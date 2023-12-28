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


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class GameController(GameControllerInterface):

    def __init__(self):
        self._role = None
        self._setup_completed = False
        self._game_data: DataControllerInterface = Game()
        self._encoder: Optional[EncoderInterface] = None
        self._decoder: Optional[DecoderInterface] = None

    def setup(self, ui: UiControllerInterface):
        if self._setup_completed:
            raise Exception("Fehler: Spiel wurde schon gestartet!")
        role = ui.prompt_for_role()
        if role.lower() == "codierer":
            self._decoder = LocalDecoder()
            self._encoder = HumanEncoder(ui)
            self._role = "codierer"
        elif role.lower() == "rater":
            if ui.prompt_for_network_encoder() == "Netzwerk":
                host = ui.prompt_for_host_addr()
                decoder_mode = ui.prompt_for_computer_decoder()
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
