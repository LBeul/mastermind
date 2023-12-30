import random

from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.encoder.encoder_interface import EncoderInterface
from superhirn.logic.util.code import Code
from superhirn.logic.util.color import Color
from superhirn.logic.util.rating import Rating


class LocalEncoder(EncoderInterface):
    def __init__(self, game_data: DataControllerInterface):
        self._game_data = game_data

    @property
    def game_data(self):
        return self._game_data

    def generate_code(self) -> Code:
        number_array = list(range(1, self._game_data.get_number_of_colors() + 1))
        random_colors = [Color(random.choice(number_array))
                         for __ in range(self._game_data.get_code_length())]
        return Code(random_colors)

    def rate(self, code_guess: Code) -> Rating:
        guess: list[int] = code_guess.to_int_list().copy()
        goal: list[int] = self._game_data.get_code().to_int_list().copy()
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

        rating_values = black + white[:-len(black)]
        rating = [Color(v) for v in rating_values]
        return Rating(rating)
