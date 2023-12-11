from typing import Optional
import random

from superhirn.data.color import Color
from superhirn.logic.decoder.decoder_interface import DecoderInterface
from superhirn.logic.decoder.local_decoder import LocalDecoder
from superhirn.logic.encoder.encoder_interface import EncoderInterface
from superhirn.logic.gamecontroller.game_controller import GameControllerInterface
from superhirn.interfaces.data_interface import DataInterface


def color_string_to_list(color_string: str) -> list[Color]:
    split_values: list[str] = color_string.split(", ")
    return [Color(val) for val in split_values]


class GameController(GameControllerInterface):
    def __init__(self):
        self._current_game_statistics: DataInterface = DataInterface()
        self._encoder: Optional[EncoderInterface] = None
        self._decoder: Optional[DecoderInterface] = None

    def get_instance(self):
        # TODO: Figure out how to create singleton in Python
        pass

    def set_game_parameters(self, human_role: str, code_length: int, available_colors: str, is_online: bool) -> None:
        if human_role.lower() == "codierer":
            self._decoder = LocalDecoder(code_length, )
