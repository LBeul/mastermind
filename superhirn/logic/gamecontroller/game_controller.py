from typing import Optional

from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.connector.ui_controller_interface import UiControllerInterface
from superhirn.logic.decoder.decoder_interface import DecoderInterface
from superhirn.logic.decoder.human_decoder import HumanDecoder
from superhirn.logic.decoder.local_decoder import LocalDecoder
from superhirn.logic.encoder.encoder_interface import EncoderInterface
from superhirn.logic.encoder.human_encoder import HumanEncoder
from superhirn.logic.encoder.local_encoder import LocalEncoder
from superhirn.logic.encoder.network_encoder import NetworkEncoder
from superhirn.logic.gamecontroller.game_controller_interface import GameControllerInterface
from superhirn.logic.util.role import Role


class GameController(GameControllerInterface):

    def __init__(self):
        self._ui = None
        self._setup_completed = False
        self._game_data = None
        self._encoder: Optional[EncoderInterface] = None
        self._decoder: Optional[DecoderInterface] = None
        self._max_turns = 10
        self._turn_counter = 1
        self._role = None

    def setup(self, ui: UiControllerInterface, game_data: DataControllerInterface):
        self._ui = ui
        self._game_data = game_data
        ui.show_start_screen()
        if self._setup_completed:
            raise Exception("Fehler: Spiel wurde schon gestartet!")
        self._role = ui.prompt_for_role()
        if self._role == Role.ENCODER:
            self._decoder = LocalDecoder(ui, game_data)
            self._encoder = HumanEncoder(ui, game_data)
        elif self._role == Role.DECODER:

            if ui.prompt_for_network_encoder():
                host = ui.prompt_for_host_addr()
                self._encoder = NetworkEncoder(game_data, host, "42")
                if ui.prompt_for_computer_decoder():
                    self._decoder = LocalDecoder(ui, game_data)
                else:
                    self._decoder = HumanDecoder(ui, game_data)
            else:
                self._encoder = LocalEncoder(game_data)
                self._decoder = HumanDecoder(ui, game_data)

        code_length = ui.prompt_for_code_length()
        self._game_data.set_code_length(code_length)
        number_of_colors = ui.prompt_for_number_of_colors()
        self._game_data.set_number_of_colors(number_of_colors)

        self._setup_completed = True

    def start(self):
        if not self._setup_completed:
            raise Exception("Fehler: Spiel wurde noch nicht initialisiert")
        win = False
        code = self._encoder.generate_code()
        self._game_data.set_code(code)
        self._ui.update_board(self._game_data.get_questions(), self._game_data.get_ratings(), self._role,
                              self._game_data.get_code())
        while self._turn_counter <= self._max_turns and win is False:
            self._turn_counter += 1
            guess = self._decoder.guess()
            self._game_data.add_question(guess)
            self._ui.update_board(self._game_data.get_questions(), self._game_data.get_ratings(), self._role,
                                  self._game_data.get_code())

            rating = self._encoder.rate(guess)
            self._game_data.add_rating(rating)
            self._ui.update_board(self._game_data.get_questions(), self._game_data.get_ratings(), self._role,
                                  self._game_data.get_code())

            if rating.count_blacks() == self._game_data.get_code_length():
                win = True

        self._ui.show_end_screen(win, self._game_data.get_code())
