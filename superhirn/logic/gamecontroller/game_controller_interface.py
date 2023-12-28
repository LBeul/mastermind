from abc import ABC, abstractmethod

from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.connector.ui_controller_interface import UiControllerInterface


class GameControllerInterface(ABC):
    @abstractmethod
    def get_instance(self):
        """
        Returns a singleton instance of the game_controller
        :return: Singleton instance
        """
        pass

    def setup(self, ui: UiControllerInterface):
        """
        Starts the game setup
        :exception: # ToDo eigene Exceptions?
        :param ui: User Interface Controller which will handle user in- and output.
        """
        pass
