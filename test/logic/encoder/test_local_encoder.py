import unittest

from superhirn.data.game import Game
from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.encoder.encoder_interface import EncoderInterface
from superhirn.logic.encoder.local_encoder import LocalEncoder
from superhirn.logic.util.code import Code
from superhirn.logic.util.color import Color


class LocalEncoderTestCase(unittest.TestCase):
    data: DataControllerInterface = Game()

    data.set_code_length(4)
    data.set_number_of_colors(3)
    data.set_code(Code([Color.RED, Color.GREEN, Color.RED, Color.GREEN]))

    invalid_colors: list[Color] = [Color.BLUE, Color.BROWN, Color.ORANGE, Color.BLACK, Color.WHITE]

    encoder: EncoderInterface = LocalEncoder(data)

    def test_generate_code(self):
        generated_code: Code = self.encoder.generate_code()
        for color in self.invalid_colors:
            self.assertNotIn(color.value, generated_code.to_int_list())
        self.assertEqual(len(generated_code.to_int_list()), self.data.get_code_length())

    def test_returns_empty_rating_for_invalid_code(self):
        attempt: Code = Code(([Color.YELLOW] * 4))
        self.assertCountEqual(self.encoder.rate(attempt).get_colors(), [])

    def test_returns_only_black_pins_if_correct_code(self):
        attempt = Code([Color.RED, Color.GREEN, Color.RED, Color.GREEN])
        self.assertCountEqual(self.encoder.rate(attempt).get_colors(), [Color.BLACK] * 4)

    def test_returns_all_white_rating_for_right_values_in_wrong_place(self):
        attempt = Code([Color.GREEN, Color.RED, Color.GREEN, Color.RED])
        self.assertCountEqual(self.encoder.rate(attempt).get_colors(), [Color.WHITE] * 4)

    def test_returns_black_pins_for_correct_values(self):
        attempt = Code([Color.RED, Color.GREEN, Color.YELLOW, Color.GREEN])
        self.assertCountEqual(self.encoder.rate(attempt).get_colors(), [Color.BLACK, Color.BLACK, Color.BLACK])

    def test_returns_mix_of_black_and_white_pins_if_partially_correct(self):
        attempt = Code([Color.RED, Color.GREEN, Color.GREEN, Color.RED])
        self.assertCountEqual(self.encoder.rate(attempt).get_colors(),
                              [Color.BLACK, Color.BLACK, Color.WHITE, Color.WHITE])
