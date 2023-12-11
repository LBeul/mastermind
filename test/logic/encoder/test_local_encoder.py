import unittest

from superhirn.data.code import Code
from superhirn.data.color import Color
from superhirn.logic.encoder.encoder_interface import EncoderInterface
from superhirn.logic.encoder.local_encoder import LocalEncoder


class LocalEncoderTestCase(unittest.TestCase):
    length: int = 5
    valid_colors: list[Color] = [Color.RED, Color.GREEN, Color.ORANGE, Color.BROWN]
    invalid_colors: list[Color] = [Color.BLUE, Color.YELLOW, Color.BLACK, Color.WHITE]
    encoder: EncoderInterface = LocalEncoder(length, valid_colors)
    generated_code: Code = encoder.generate_code()

    def test_generate_code(self):
        self.assertEqual(len(self.generated_code.to_int_list()), self.length)
        for color in self.invalid_colors:
            self.assertNotIn(color.value, self.generated_code.to_int_list())

    def test_rate_code(self):
        invalid_code: Code = Code([Color.BLUE] * 5)
        self.assertCountEqual(self.encoder.rate(invalid_code).to_int_list(), [None] * 5)

        valid_code = self.generated_code
        self.assertCountEqual(self.encoder.rate(valid_code).to_int_list(), [Color.BLACK] * 5)
