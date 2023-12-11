import random
from superhirn.logic.encoder.encoder_interface import EncoderInterface
from superhirn.data.color import Color
from superhirn.data.code import Code


class LocalEncoder(EncoderInterface):
    def __init__(self, code_length: int, available_colors: list[Color]):
        self._code_length = code_length
        self._available_colors = available_colors
        self._generated_code = None

    def generate_code(self) -> Code:
        random_colors = [random.choice(self._available_colors) for __ in range(self._code_length)]
        self._generated_code = Code(random_colors)
        return self._generated_code

    def rate(self, code_guess) -> Code:
        rating: Code
        pass
