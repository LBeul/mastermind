from abc import ABC, abstractmethod

from superhirn.logic.util.code import Code


class DecoderInterface(ABC):
    @abstractmethod
    def guess(self, code_length: int, color_availabilities: int) -> Code:
        """
        Generates a code guess of the given length, using the available colors
        :param code_length: Length of the new guess.
        :param color_availabilities: number of colors of the new guess.
        :return: the newly generated Code instance
        """
        pass
