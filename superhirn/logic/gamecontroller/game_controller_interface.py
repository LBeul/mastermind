from abc import ABC, abstractmethod

from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.connector.ui_controller_interface import UiControllerInterface


class GameControllerInterface(ABC):

    @abstractmethod
    def get_data(self) -> DataControllerInterface:
        """
        Returns the current used DataController, which will be used to set and get data
        :return: DataInterface to controll
        """
        pass

    @abstractmethod
    def setup(self, ui: UiControllerInterface):
        """
        Starts the game setup
        :exception: # ToDo eigene Exceptions?
        :param ui: User Interface Controller which will handle user in- and output.
        """
        pass
