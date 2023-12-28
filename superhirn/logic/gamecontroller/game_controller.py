from typing import Optional

from superhirn.data.game import Game
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
from superhirn.view.client import Client


def color_string_to_list(color_string: str) -> list[Color]:
    return [Color(int(val)) for val in color_string]


class GameController(GameControllerInterface):
    def __init__(self):
        self._role = None
        self._setup_completed = False
        self._game_data: DataControllerInterface = Game()
        self._encoder: Optional[EncoderInterface] = None
        self._decoder: Optional[DecoderInterface] = None

    def main_loop(self):
        ui = Client()
        ui.show_menu()
        while True:
            if self._setup_completed:
                self.game_loop(ui)
                break
            command = input("Befehl: ").lower()
            if command == 'help':
                ui.show_help()
            elif command == 'start':
                ui.clear_screen()
                self.setup(ui)
            elif command == 'exit':
                exit()
            else:
                print("Ungültige Eingabe.")

    def game_loop(self, ui: UiControllerInterface):
        self._encoder.generate_code(self._game_data.get_code_length(), self._game_data.get_number_of_colors())
        for i in range(10):
            ui.clear_screen()
            ui.show_game_view(self._game_data.get_questions(), self._game_data.get_ratings(), self._role,
                              str(self._game_data.get_code()))
            self._game_data.add_question(
                self._decoder.guess(self._game_data.get_code_length(), self._game_data.get_number_of_colors()))
            self._game_data.add_rating(self._encoder.rate(self._game_data.get_code()))

    def setup(self, ui: UiControllerInterface):
        if self._setup_completed:
            raise Exception("Fehler: Spiel wurde schon gestartet!")
        role = ui.prompt_for_role()
        if role.lower() == "codierer":
            self._decoder = LocalDecoder()
            self._encoder = HumanEncoder(ui)
            self._role = "codierer"
        elif role.lower() == "rater":
            if ui.prompt_for_encoder() == "Netzwerk":
                host = ui.prompt_for_connection()
                decoder_mode = ui.prompt_for_decoder()
                if decoder_mode == "Selbst":
                    self._encoder = NetworkEncoder(host)
                    self._decoder = HumanDecoder(ui)
                elif decoder_mode == "Computer":
                    self._encoder = NetworkEncoder(host)
                    self._decoder = LocalDecoder()
                self._role = "rater"
            else:
                self._encoder = LocalEncoder()
                self._decoder = HumanDecoder(ui)
        # ToDO String der richtiger Typ? boolean oder int könnte besser sein oder ENUM?

        code_length = ui.prompt_for_code_length()
        self._game_data.set_code_length(code_length)
        color_amount = ui.prompt_for_number_of_colors()
        self._game_data.set_number_of_colors(color_amount)

        code = self._encoder.generate_code(self._game_data.get_code_length(),
                                           self._game_data.get_number_of_colors())
        self._game_data.set_code(code)

        self._setup_completed = True

    def get_data(self) -> DataControllerInterface:
        return self._game_data
