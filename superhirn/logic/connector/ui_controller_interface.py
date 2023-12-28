from abc import ABC, abstractmethod

from superhirn.logic.util.code import Code
from superhirn.logic.util.rating import Rating
from superhirn.logic.util.role import Role


class UiControllerInterface(ABC):

    @abstractmethod
    def update_board(self, questions: list, ratings: list, role: str, code: str):
        """
        Updates the current game-board.
        :param code: code of the current game.
        :param role: Role of the player.
        :param ratings: Already given ratings as a list.
        :param questions: Already given questions as a list.
        """
        pass

    @abstractmethod
    def prompt_for_role(self) -> Role:
        """
        Prompts the user to select a role.

        :return: selected role.
        """
        pass

    @abstractmethod
    def prompt_for_network_encoder(self) -> bool:
        """
        Prompts the user to select the encoder type.

        :return: true for network, false for local.
        """
        pass

    def prompt_for_computer_decoder(self) -> bool:
        """
        Prompts the user to select decoder type.

        :return: true for computer, false for human.
        """
        pass

    @abstractmethod
    def prompt_for_host_addr(self) -> str:
        """
        Prompts the user to set the connection address.

        :return: host address in format ip:port.
        """
        pass

    @abstractmethod
    def prompt_for_code_length(self) -> int:
        """
        Prompts the user to set the code length.
        4 or 5 is valid.

        :return: selected length.
        """
        pass

    @abstractmethod
    def prompt_for_number_of_colors(self) -> int:
        """
        Prompts the user to set the number of colors.
        2 to 8 is valid.

        :return: selected number of colors.
        """
        pass

    @abstractmethod
    def prompt_for_code(self, code_length: int, number_of_colors: int) -> Code:
        """
        Prompts the user to set the code.
        Prints help for number_of_colors.

        :return: selected code.
        """
        pass

    @abstractmethod
    def prompt_for_guess(self, code_length: int, number_of_colors: int) -> Code:
        """
        Prompts the user to give a guess.

        :return: given guess.
        """
        pass

    @abstractmethod
    def prompt_for_rating(self, code_length: int) -> Rating:
        """
        Prompts the user to give a rating.

        :return: given rating.
        """
        pass

    @abstractmethod
    def show_end_screen(self, win: bool, code: Code):
        """
        Shows the end screen for the player.
        :param code: Code of the current game.
        :param win: True for win, false for defeat.
        """
        pass
