from typing import Optional
import random

from superhirn.data.color import Color
from superhirn.logic.decoder.decoder_interface import DecoderInterface
from superhirn.logic.decoder.local_decoder import LocalDecoder
from superhirn.logic.encoder.encoder_interface import EncoderInterface
from superhirn.logic.encoder.local_encoder import LocalEncoder
from superhirn.logic.encoder.network_encoder import NetworkEncoder
from superhirn.logic.gamecontroller.game_controller_interface import GameControllerInterface
from superhirn.interfaces.data_interface import DataInterface


def color_string_to_list(color_string: str) -> list[Color]:
    split_values: list[str] = color_string.split(",")
    return [Color(int(val)) for val in split_values]


class GameController(GameControllerInterface):
    def __init__(self):
        self._setup_completed = False
        self._current_game_statistics: DataInterface = DataInterface()
        self._encoder: Optional[EncoderInterface] = None
        self._decoder: Optional[DecoderInterface] = None

    def get_instance(self):
        # TODO: Figure out how to create singleton in Python
        pass

    def set_game_parameters(self, human_role: str, code_length: int, available_colors: str, is_online: bool,
                            ip_address: str = None, port: int = None):
        if self._setup_completed:
            raise Exception("Error: Game was already set up!")

        valid_colors: list[Color] = color_string_to_list(available_colors)

        if human_role.lower() == "codierer":
            self._decoder = LocalDecoder(code_length, valid_colors)
        elif human_role.lower() == "rater":
            if not is_online:
                self._encoder = LocalEncoder(code_length, valid_colors)
            else:
                self._encoder = NetworkEncoder(code_length, valid_colors, ip_address, port)
        else:
            raise Exception("Please choose either 'Rater' or 'Codierer' as role")

        self._setup_completed = True
