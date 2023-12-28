import random

from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.encoder.encoder_interface import EncoderInterface
from superhirn.logic.util.code import Code
from superhirn.logic.util.color import Color
from superhirn.logic.util.rating import Rating


class LocalEncoder(EncoderInterface):
    def __init__(self):
        self._generated_code = None

    def generate_code(self, code_length: int, color_availabilities: int) -> Code:
        number_array = list(range(1, color_availabilities + 1))
        random_colors = [random.choice(number_array)
                         for __ in range(self._game_data.get_code_length())]
        return Code(random_colors)

    def rate(self, code_guess: Code) -> Rating:
        guess: str = code_guess.to_int_string()
        goal: str = self._game_data.get_code().to_int_string()

        black = 0
        white = len(set(guess) & set(goal)) - black

        for x in range(self._game_data.get_code_length()):
            if guess[x] == goal[x]:
                black += 1

        rating = ([Color.BLACK] * black) + ([Color.WHITE] * white)
        return Rating(rating)
