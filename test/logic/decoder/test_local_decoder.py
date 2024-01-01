import unittest

from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.decoder.local_decoder import LocalDecoder
from superhirn.logic.util.code import Code


class MockDataController(DataControllerInterface):
    def __init__(self, code_length, number_of_colors):
        self._code_length = code_length
        self._number_of_colors = number_of_colors
        self._questions = []
        self._ratings = []

    # Implement all abstract methods
    def set_code(self, given_code: Code):
        pass

    def get_code(self) -> Code:
        pass

    def set_code_length(self, given_code_length: int):
        pass

    def get_code_length(self) -> int:
        return self._code_length

    def set_number_of_colors(self, given_number_of_colors):
        pass

    def get_number_of_colors(self) -> int:
        return self._number_of_colors

    def add_question(self, given_question: Code):
        self._questions.append(given_question)

    def get_questions(self) -> list[Code]:
        return self._questions

    def add_rating(self, given_rating):
        self._ratings.append(given_rating)

    def get_ratings(self):
        return self._ratings


class LocalDecoder4PegsTestCase(unittest.TestCase):
    def setUp(self):
        self.data_controller = MockDataController(4, 6)
        self.decoder = LocalDecoder(self.data_controller)

    def test_initial_guess(self):
        guess = self.decoder.guess()
        self.assertEqual(len(guess.to_int_list()), 4, "Initial guess should be 4 pegs long.")

    def test_guess_color_range(self):
        guess = self.decoder.guess()
        for color in guess.to_int_list():
            self.assertTrue(1 <= color <= 6, "Color should be within the valid range.")


class LocalDecoder5PegsTestCase(unittest.TestCase):
    def setUp(self):
        self.data_controller = MockDataController(5, 6)  # 5 pegs, 6 colors
        self.decoder = LocalDecoder(self.data_controller)

    def test_initial_guess(self):
        guess = self.decoder.guess()
        self.assertEqual(len(guess.to_int_list()), 5, "Initial guess should be 5 pegs long.")

    def test_guess_color_range(self):
        guess = self.decoder.guess()
        for color in guess.to_int_list():
            self.assertTrue(1 <= color <= 6, "Color should be within the valid range.")


if __name__ == '__main__':
    unittest.main()
