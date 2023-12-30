from abc import ABC, abstractmethod

from superhirn.logic.util.code import Code


class DecoderInterface(ABC):

    @property
    @abstractmethod
    def game_data(self):
        pass

    @abstractmethod
    def guess(self) -> Code:
        """
        Generates a code guess of the given length, using the available colors
        :return: the newly generated Code instance
        """
        pass
