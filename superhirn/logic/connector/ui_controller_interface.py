from abc import ABC, abstractmethod


class UiControllerInterface(ABC):

    @abstractmethod
    def prompt_for_role(self) -> str:
        """
        Prompts the user to select a role.

        :return: selected role.
        """
        pass

    @abstractmethod
    def prompt_for_encoder(self) -> str:
        """
        Prompts the user to select the encoder type.

        :return: selected type.
        """
        pass

    def prompt_for_decoder(self) -> str:
        """
        Prompts the user to select decoder type.

        :return: selected type.
        """
        pass

    @abstractmethod
    def prompt_for_connection(self) -> str:
        """
        Prompts the user to set the connection address.
        ip:port

        :return: selected role.
        """
        pass

    @abstractmethod
    def prompt_for_code_length(self) -> int:
        """
        Prompts the user to set the code length.
        4 or 5 is valid

        :return: selected length.
        """
        pass

    @abstractmethod
    def prompt_for_number_of_colors(self) -> int:
        """
        Prompts the user to set the amount of colors.
        2 to 8 is valid

        :return: selected amount.
        """
        pass

    @abstractmethod
    def prompt_for_code(self, code_length: int, color_amount: int) -> str:
        """
        Prompts the user to set the code.
        Prints help for available_colors.

        :return: selected code.
        """
        pass

    @abstractmethod
    def prompt_for_guess(self, code_length: int, color_amount: int) -> str:
        """
        Prompts the user to give a guess.

        :return: given guess.
        """
        pass

    @abstractmethod
    def prompt_for_rating(self, code_length: int) -> str:
        """
        Prompts the user to give a rating.

        :return: given rating.
        """
        pass
