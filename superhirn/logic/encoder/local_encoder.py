import random

from superhirn.data.code import Code
from superhirn.data.data_interface import DataInterface
from superhirn.logic.encoder.encoder_interface import EncoderInterface


class LocalEncoder(EncoderInterface):
    def __init__(self, game_data: DataInterface):
        self._generated_code = None
        self._game_data = game_data

    def generate_code(self) -> Code:
        number_array = list(range(1, self._game_data.get_color_availabilities() + 1))
        random_colors = [random.choice(number_array)
                         for __ in range(self._game_data.get_code_length())]
        self._generated_code = Code(random_colors)
        return self._generated_code

    def rate(self, code_guess) -> Code:
        rating: Code
        pass
