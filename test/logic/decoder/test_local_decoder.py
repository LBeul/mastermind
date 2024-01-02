import unittest

from superhirn.logic import Color
from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.connector.ui_controller_interface import UiControllerInterface
from superhirn.logic.decoder.local_decoder import LocalDecoder
from superhirn.logic.util.code import Code
from superhirn.logic.util.rating import Rating
from superhirn.logic.util.role import Role


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


class MockUiController(UiControllerInterface):
    def update_board(self, questions: list, ratings: list, role: str, code: str):
        pass

    def prompt_for_role(self) -> Role:
        pass

    def prompt_for_network_encoder(self) -> bool:
        pass

    def prompt_for_host_addr(self) -> str:
        pass

    def prompt_for_code_length(self) -> int:
        pass

    def prompt_for_number_of_colors(self) -> int:
        pass

    def prompt_for_code(self, code_length: int, number_of_colors: int) -> Code:
        pass

    def prompt_for_guess(self, code_length: int, number_of_colors: int) -> Code:
        pass

    def prompt_for_rating(self, code_length: int) -> Rating:
        pass

    def show_end_screen(self, win: bool, code: Code):
        pass

    def show_start_screen(self):
        pass

    def prompt_for_error_in_rating(self):
        pass


class LocalDecoder4PegsTestCase(unittest.TestCase):
    def setUp(self):
        self.data_controller = MockDataController(4, 6)
        self.ui_controller = MockUiController()
        self.decoder = LocalDecoder(self.ui_controller, self.data_controller)

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
        self.ui_controller = MockUiController()
        self.decoder = LocalDecoder(self.ui_controller, self.data_controller)

    def test_initial_guess(self):
        guess = self.decoder.guess()
        self.assertEqual(len(guess.to_int_list()), 5, "Initial guess should be 5 pegs long.")

    def test_guess_color_range(self):
        guess = self.decoder.guess()
        for color in guess.to_int_list():
            self.assertTrue(1 <= color <= 6, "Color should be within the valid range.")


class LocalDecoderInitTestPossibleCodes(unittest.TestCase):
    def setUp(self):
        self.data_controller = MockDataController(5, 3)
        self.ui_controller = MockUiController()
        self.decoder = LocalDecoder(self.ui_controller, self.data_controller)

    def test_initialize_possible_codes(self):
        self.assertEqual(len(self.decoder._LocalDecoder__initialize_possible_codes()), 243)


class LocalDecoderInitTestPossibleCodes2(unittest.TestCase):
    def setUp(self):
        self.data_controller = MockDataController(6, 4)
        self.ui_controller = MockUiController()
        self.decoder = LocalDecoder(self.ui_controller, self.data_controller)

    def test_initialize_possible_codes(self):
        self.assertEqual(len(self.decoder._LocalDecoder__initialize_possible_codes()), 4096)


class LocalDecoderInitTestPossibleCodes3(unittest.TestCase):
    def setUp(self):
        self.data_controller = MockDataController(8, 6)
        self.ui_controller = MockUiController()
        self.decoder = LocalDecoder(self.ui_controller, self.data_controller)

    def test_initialize_possible_codes(self):
        self.assertEqual(len(self.decoder._LocalDecoder__initialize_possible_codes()), 1679616)


class LocalDecoderFilterPossibleCodes(unittest.TestCase):
    def setUp(self):
        self.data_controller = MockDataController(8, 6)
        self.ui_controller = MockUiController()
        self.decoder = LocalDecoder(self.ui_controller, self.data_controller)

    def test_filter_possible_codes(self):
        self.decoder._LocalDecoder__filter_possible_codes(1234, {2, 2})
        self.assertTrue(len(self.decoder._possible_codes) < 1679616, "smaller than the max amount")


class LocalDecoderRateGuess(unittest.TestCase):
    def setUp(self):
        self.data_controller = MockDataController(8, 6)
        self.ui_controller = MockUiController()
        self.decoder = LocalDecoder(self.ui_controller, self.data_controller)

    def test_rate_guess(self):
        self.assertEqual(self.decoder._LocalDecoder__rate_guess((1, 2, 3, 4), (1, 2, 3, 4))._colors,
                         [Color.BLACK, Color.BLACK, Color.BLACK, Color.BLACK])


class LocalDecoderRateGuess2(unittest.TestCase):
    def setUp(self):
        self.data_controller = MockDataController(8, 6)
        self.ui_controller = MockUiController()
        self.decoder = LocalDecoder(self.ui_controller, self.data_controller)

    def test_rate_guess(self):
        self.assertEqual(self.decoder._LocalDecoder__rate_guess((1, 2, 4, 3), (1, 2, 3, 4))._colors,
                         [Color.BLACK, Color.BLACK, Color.WHITE, Color.WHITE])


if __name__ == '__main__':
    unittest.main()
