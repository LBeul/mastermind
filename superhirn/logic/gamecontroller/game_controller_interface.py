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
    def set_game_parameters(self, human_role: str, code_length: int, available_colors: str, is_online: bool) -> None:
        """
        Sets the initial parameters for the Game to be started
        :param human_role: the role taken by the user
        :param code_length: the fixed code length of the game
        :param available_colors: the colors available to compose the Code of
        :param is_online: indicates whether the game shall take place locally or against a remote server encoder
        """
        pass
