import unittest

from superhirn.logic.decoder.decoder_interface import DecoderInterface
from superhirn.logic.decoder.local_decoder import LocalDecoder
from superhirn.logic.util.code import Code
from superhirn.logic.util.color import Color


class LocalDecoderTestCase(unittest.TestCase):
    length: int = 5
    valid_colors: list[Color] = [Color.RED, Color.GREEN, Color.ORANGE, Color.BROWN]
    invalid_colors: list[Color] = [Color.BLUE, Color.YELLOW, Color.BLACK, Color.WHITE]
    decoder: DecoderInterface = LocalDecoder(length, valid_colors)
    attempt: Code = decoder.guess()

    def test_guess(self):
        self.assertEqual(len(self.attempt.to_int_list()), self.length)
        for color in self.invalid_colors:
            self.assertNotIn(color.value, self.attempt.to_int_list())
