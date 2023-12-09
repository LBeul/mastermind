from superhirn.data.code import Code
from superhirn.data.rating import Rating
from superhirn.interfaces.data_interface import DataInterface


class Game(DataInterface):
    code = None
    code_length = None
    color_availabilities = None
    questions = []
    ratings = []

    def set_code(self, given_code: Code):
        """
        Sets the game code.
        :param given_code: Code which will be set
        """
        self.code = given_code

    def set_code_length(self, given_code_length: int):
        """
        Sets the code length of the game.
        :param given_code_length: Code length as int
        """
        self.code_length = given_code_length

    def set_color_availabilities(self, given_color_availabilities):
        """
        Sets the amount of colors, which will be used in the game
        :param given_color_availabilities: Amount of colors as int
        """
        self.color_availabilities = given_color_availabilities

    def add_question(self, given_question: Code):
        """
        Adds a question to the list
        :param given_question: Code which will be added
        """
        self.questions.append(given_question)

    def add_rating(self, given_rating: Rating):
        """
        Adds a rating to the list
        :param given_rating: Code which will be added
        """
        self.ratings.append(given_rating)
