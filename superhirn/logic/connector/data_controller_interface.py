from abc import abstractmethod

from superhirn.data.code import Code
from superhirn.data.rating import Rating


class DataControllerInterface:

    @abstractmethod
    def set_code(self, given_code: Code):
        """
        Sets the game code.
        :param given_code: Code which will be set
        """
        pass

    @abstractmethod
    def get_code(self) -> Code:
        """
        Gets the game code.
        :return: Code.
        """
        pass

    @abstractmethod
    def set_code_length(self, given_code_length: int):
        """
        Sets the code length of the game.
        :param given_code_length: Code length as int
        """
        pass

    @abstractmethod
    def get_code_length(self) -> int:
        """
        Gets the code length of the game.
        :return: Code length as int.
        """
        pass

    @abstractmethod
    def set_number_of_colors(self, given_number_of_colors):
        """
        Sets the amount of colors, which will be used in the game.
        :param given_number_of_colors: Amount of colors as int.
        """
        pass

    @abstractmethod
    def get_number_of_colors(self) -> int:
        """
        Gets the amount of colors, which will be used in the game.
        :return: Amount of colors as int.
        """
        pass

    @abstractmethod
    def add_question(self, given_question: Code):
        """
        Adds a question to the list
        :param given_question: Code which will be added.
        """
        pass

    @abstractmethod
    def get_questions(self) -> list:
        """
        Gets the questions.
        :return: All questions.
        """
        pass

    @abstractmethod
    def add_rating(self, given_rating: Rating):
        """
        Adds a rating to the list.
        :param given_rating: Code which will be added.
        """
        pass

    @abstractmethod
    def get_ratings(self) -> list:
        """
        Gets the ratings.
        :return: All ratings.
        """
        pass
