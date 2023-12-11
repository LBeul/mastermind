from abc import ABC, abstractmethod


class GameControllerInterface(ABC):
    @abstractmethod
    def get_instance(self):
        """
        Returns a singleton instance of the game_controller
        :return: Singleton instance
        """
        pass

    @abstractmethod
    def start_game(self, human_role, online):
        """
        Initiates new game and sets role and online params
        :param online: indicates whether game takes place on- or offline
        :param human_role: the role chosen by the player
        :return: void
        """
        pass

    @abstractmethod
    def get_game_state(self):
        """
        :return: current state of the game
        """
        pass
