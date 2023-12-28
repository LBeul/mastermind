import random

from superhirn.data.code import Code
from superhirn.data.rating import Rating
from superhirn.logic.encoder.encoder_interface import EncoderInterface


class LocalEncoder(EncoderInterface):
    def __init__(self):
        self._generated_code = None

    def generate_code(self, code_length: int, color_availabilities: int) -> Code:
        number_array = list(range(1, color_availabilities + 1))
        random_colors = [random.choice(number_array)
                         for __ in range(code_length)]
        self._generated_code = Code(random_colors)
        return self._generated_code

    def rate(self, code_guess) -> Rating:
        rating: Code
        pass
