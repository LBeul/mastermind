from typing import Optional

from superhirn.data.code import Code
from superhirn.data.color import Color
from superhirn.data.data_interface import DataInterface
from superhirn.data.game import Game
from superhirn.logic.decoder.decoder_interface import DecoderInterface
from superhirn.logic.decoder.local_decoder import LocalDecoder
from superhirn.logic.encoder.encoder_interface import EncoderInterface
from superhirn.logic.encoder.local_encoder import LocalEncoder
from superhirn.logic.encoder.network_encoder import NetworkEncoder
from superhirn.logic.gamecontroller.game_controller_interface import GameControllerInterface
from superhirn.logic.ui_connector.ui_connector_interface import UiControllerInterface


def color_string_to_list(color_string: str) -> list[Color]:
    return [Color(int(val)) for val in color_string]


class GameController(GameControllerInterface):
    def __init__(self):
        self._setup_completed = False
        self._game_data: DataInterface = Game()
        self._encoder: Optional[EncoderInterface] = None
        self._decoder: Optional[DecoderInterface] = None

    def get_instance(self):
        # TODO: Figure out how to create singleton in Python
        pass

    def setup(self, ui: UiControllerInterface):
        if self._setup_completed:
            raise Exception("Fehler: Spiel wurde schon gestartet!")
        role = ui.prompt_for_role()
        if role.lower() == "codierer":
            self._decoder = LocalDecoder(self._game_data)
        elif role.lower() == "rater":
            if ui.prompt_for_encoder_mode() == "Netzwerk":
                host = ui.prompt_for_connection()
                self._encoder = NetworkEncoder(host)
            else:
                self._encoder = LocalEncoder(self._game_data)
        # ToDO String der richtiger Typ? boolean oder int könnte besser sein oder ENUM?

        code_length = ui.prompt_for_code_length()
        self._game_data.set_code_length(code_length)
        color_amount = ui.prompt_for_color_amount()
        self._game_data.set_color_availabilities(color_amount)
        if role == "Codierer":
            code = ui.prompt_for_code(code_length, color_amount)
            self._game_data.set_code(Code(color_string_to_list(code)))
            print(self._game_data.get_code())
        else:
            code = self._encoder.generate_code()
            self._game_data.set_code(code)
        self._setup_completed = True
