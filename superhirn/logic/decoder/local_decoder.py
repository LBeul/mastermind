import random

from superhirn.data.code import Code
from superhirn.data.color import Color
from superhirn.logic.decoder.decoder_interface import DecoderInterface


class LocalDecoder(DecoderInterface):
    def __init__(self, code_length: int, available_colors: list[Color]):
        self._code_length = code_length
        self._available_colors = available_colors
        self._attempts: list[Code] = []

    def guess(self):
        random_colors = [random.choice(self._available_colors) for __ in range(self._code_length)]
        attempt = Code(random_colors)
        self._attempts.append(attempt)
        return attempt
