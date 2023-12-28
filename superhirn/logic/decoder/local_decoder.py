import random

from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.decoder.decoder_interface import DecoderInterface
from superhirn.logic.util.code import Code


class LocalDecoder(DecoderInterface):
    def __init__(self):
        self._attempts: list[Code] = []

    def guess(self):
        number_array = list(range(1, self._game_data.get_number_of_colors() + 1))
        random_colors = [random.choice(number_array)
                         for __ in range(self._game_data.get_code_length())]
        attempt = Code(random_colors)
        self._attempts.append(attempt)
        return attempt
