import random

from superhirn.data.code import Code
from superhirn.logic.decoder.decoder_interface import DecoderInterface


class LocalDecoder(DecoderInterface):
    def __init__(self, game_data: DataInterface):
        self._attempts: list[Code] = []
        self._game_data = game_data

    def guess(self):
        number_array = list(range(1, self._game_data.get_color_availabilities() + 1))
        random_colors = [random.choice(number_array)
                         for __ in range(self._game_data.get_code_length())]
        attempt = Code(random_colors)
        self._attempts.append(attempt)
        return attempt
