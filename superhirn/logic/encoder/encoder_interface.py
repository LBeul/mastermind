from abc import ABC, abstractmethod


class EncoderInterface(ABC):
    @abstractmethod
    def generate_code(self):
        """
        Generates a code of the given length and available colors
        :return: the newly generated Code instance
        """
        pass

    @abstractmethod
    def rate(self, code_guess):
        """
        Compares a code guess made by the Decoder against the actual code
        :return: the rating of the two codes compared to each other
        """
        pass
