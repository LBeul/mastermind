import unittest

from superhirn.data.game import Game
from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.decoder.decoder_interface import DecoderInterface
from superhirn.logic.decoder.local_decoder import LocalDecoder
from superhirn.logic.util.code import Code
from superhirn.logic.util.color import Color


class LocalDecoderTestCase(unittest.TestCase):
    data: DataControllerInterface = Game()
    data.set_code_length(5)
    data.set_number_of_colors(3)
    valid_colors: list[Color] = [Color.RED, Color.GREEN, Color.YELLOW]
    invalid_colors: list[Color] = [Color.BLUE, Color.BROWN, Color.ORANGE, Color.BLACK, Color.WHITE]
    decoder: DecoderInterface = LocalDecoder(data)
    attempt: Code = decoder.guess()

    def test_guess(self):
        self.assertEqual(len(self.attempt.to_int_list()), self.data.get_code_length())
        for color in self.invalid_colors:
            self.assertNotIn(color.value, self.attempt.to_int_list())
