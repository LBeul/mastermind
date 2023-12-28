import random

from superhirn.logic.decoder.decoder_interface import DecoderInterface
from superhirn.logic.util.code import Code


class LocalDecoder(DecoderInterface):
    def __init__(self):
        self._attempts: list[Code] = []

    def guess(self, code_length: int, color_availabilities: int):
        number_array = list(range(1, color_availabilities + 1))
        random_colors = [random.choice(number_array)
                         for __ in range(code_length)]
        attempt = Code(random_colors)
        self._attempts.append(attempt)
        return attempt
