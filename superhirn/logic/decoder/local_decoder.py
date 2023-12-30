import random

from superhirn.logic import Color
from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.decoder.decoder_interface import DecoderInterface
from superhirn.logic.util.code import Code


class LocalDecoder(DecoderInterface):
    def __init__(self, game_data: DataControllerInterface):
        self._attempts: list[Code] = []
        self._game_data = game_data

    @property
    def game_data(self):
        return self._game_data

    def guess(self):
        number_array = list(range(1, self._game_data.get_number_of_colors() + 1))
        random_colors = [Color(random.choice(number_array))
                         for __ in range(self._game_data.get_code_length())]
        attempt = Code(random_colors)
        self._attempts.append(attempt)
        return attempt
