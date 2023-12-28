from abc import ABC, abstractmethod

from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.connector.ui_controller_interface import UiControllerInterface


class GameControllerInterface(ABC):

    @abstractmethod
    def setup(self, ui: UiControllerInterface, game_data: DataControllerInterface):
        """
        Starts the game setup
        :param game_data: Game Data Interface Controller which will handle the game data.
        :exception: # ToDo eigene Exceptions?
        :param ui: User Interface Controller which will handle user in- and output.
        """
        pass
