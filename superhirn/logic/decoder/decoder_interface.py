from abc import ABC, abstractmethod


class DecoderInterface(ABC):
    @abstractmethod
    def guess(self):
        """
        Generates a code guess of the given length, using the available colors
        :return: the newly generated Code instance
        """
        pass
