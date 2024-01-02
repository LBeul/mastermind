import itertools
import random

from superhirn.logic import Color
from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.connector.ui_controller_interface import UiControllerInterface
from superhirn.logic.decoder.decoder_interface import DecoderInterface
from superhirn.logic.util.code import Code
from superhirn.logic.util.rating import Rating


class LocalDecoder(DecoderInterface):
    def __init__(self, ui: UiControllerInterface, game_data: DataControllerInterface):
        self._game_data = game_data
        self._ui = ui
        self._possible_codes = set()
        self._attempts = []
        self.rating_cache = {}

    @property
    def game_data(self):
        return self._game_data

    def __initialize_possible_codes(self):
        """
        Create a Set of all possible Code Variations possible in the requested Game configuration
        :return: Set with all Codevariations
        """
        color_numbers = range(1, self.game_data.get_number_of_colors() + 1)
        all_color_combinations = itertools.product(color_numbers, repeat=self.game_data.get_code_length())

        return set(all_color_combinations)

    def guess(self):
        if not self._possible_codes:
            self._possible_codes = self.__initialize_possible_codes()
        if not self._attempts:
            # Consider optimizing this initial guess
            n = self._game_data.get_code_length()
            num_ones = n // 2 + n % 2  # Add 1 more 1 if n is odd
            num_twos = n // 2
            current_guess = tuple([1] * num_ones + [2] * num_twos)
        else:
            last_guess = self._attempts[-1]
            last_rating = self.game_data.get_ratings()[-1]
            self.__filter_possible_codes(last_guess, last_rating)
            current_guess = self.__next_guess_based_on_minimax()

        self._attempts.append(current_guess)
        return Code([Color(number) for number in current_guess])

    def __filter_possible_codes(self, last_guess, last_rating):
        """
        Deletes all impossible Codes from the possible Codes Set after a Rating was given
        :param last_guess: previous Guss
        :param last_rating: previous Rating
        :return: Set of all still possible Code Variations
        """
        tmp_possible_codes = []
        for code in self._possible_codes:
            rating = self.__rate_guess(last_guess, code)
            if rating.count_blacks() == last_rating.count_blacks() and rating.count_whites() == last_rating.count_whites():
                tmp_possible_codes.append(code)
        self._possible_codes = tmp_possible_codes

    def __rate_guess(self, code_guess: tuple[int], code: tuple[int]):
        """
        internal Helper Function to simulate a Rating for the given Codes
        :param code_guess: the question of the decoder
        :param code: the set code of the game
        :return: a rating of the provided guess(question)
        """
        # performance boost using a cache for already computed variations
        cache_key = (code_guess, code)
        if cache_key in self.rating_cache:
            return self.rating_cache[cache_key]

        guess: list[int] = list(code_guess)
        goal: list[int] = list(code)

        black = [
            8
            for actual, guessed in zip(goal, guess)
            if actual == guessed
        ]

        white = []
        for guessed_value in guess:
            if guessed_value in goal:
                index = goal.index(guessed_value)
                goal[index] = 0
                white.append(7)

        rating_values = black + white[:len(white) - len(black)]
        rating = Rating([Color(v) for v in rating_values])

        self.rating_cache[cache_key] = rating

        return rating

    def __next_guess_based_on_minimax(self):
        """
        Calculates the next guess based on the minimax algorithm
        :return: next best guess
        """
        if not self._possible_codes:
            self._ui.prompt_for_error_in_rating()

        if len(self._possible_codes) == 1:
            return next(iter(self._possible_codes))

        min_max_score = float('inf')
        best_guess = next(iter(self._possible_codes))

        sample = random.sample(self._possible_codes, min(1500, len(self._possible_codes)))

        for guess in sample:
            score_counts = {}

            for code in sample:
                feedback = self.__rate_guess(guess, code)
                feedback_key = (feedback.count_blacks(), feedback.count_whites())
                score_counts[feedback_key] = score_counts.get(feedback_key, 0) + 1

            max_score = max(score_counts.values())
            if max_score < min_max_score:
                min_max_score = max_score
                best_guess = guess

        return best_guess
