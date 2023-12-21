from abc import ABC, abstractmethod

from superhirn.data.code import Code


class EncoderInterface(ABC):
    @abstractmethod
    def generate_code(self, code_length: int, color_availabilities: int) -> Code:
        """
        Generates a code of the given length and available colors
        :param code_length: length of the to be generated code.
        :param color_availabilities: number of colors of the to be generated code.
        :return: the newly generated Code instance
        """
        pass

    @abstractmethod
    def rate(self, code_guess: Code) -> Code:
        """
        Rates a code attempt by comparing it to the actual code and giving color-coded feedback:
        - BLACK values for each right guess (position and color)
        - WHITE values for right colors that are wrongly placed
        - None for invalid guesses
        :param code_guess: the guess made by the user
        :return: A Code instance with BLACK, WHITE or None values
        """
        pass
