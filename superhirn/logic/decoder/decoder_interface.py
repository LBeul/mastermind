from abc import ABC, abstractmethod

from superhirn.data.code import Code


class DecoderInterface(ABC):
    @abstractmethod
    def guess(self) -> Code:
        """
        Generates a code guess of the given length, using the available colors
        :return: the newly generated Code instance
        """
        pass
