import os
import re
from abc import ABC

from superhirn.logic.connector.ui_controller_interface import UiControllerInterface
from superhirn.logic.util.code import Code
from superhirn.logic.util.color import Color
from superhirn.logic.util.rating import Rating
from superhirn.logic.util.role import Role


class Client(UiControllerInterface, ABC):

    def __check_for_ui_command(self, input_string: str) -> bool:
        """
        Help function to check input for game commands.
        :param input_string:
        :return: true if command was found, false if no command was found.
        """
        if input_string == "help":
            self.__show_help()
            return True
        elif input_string == "exit":
            exit()
        return False

    def __clear_screen(self):
        """
        Helper function to clean the terminal screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def __show_help(self):
        """
        Shows the help page.
        """
        print("--------------------------------------------------")
        print("Spielanleitung")
        print("--------------------------------------------------")
        print("Anleitung 1,2,3")
        print("--------------------------------------------------")
        print("'help' zum Anzeigen der Spielanleitung")
        print("'exit' zum Beenden")
        print("--------------------------------------------------")

    def update_board(self, questions: list, ratings: list, role: str, code: str):
        questions.reverse()
        ratings.reverse()
        output = zip(questions, ratings)
        print("Spielfeld")
        print("--------------------------------------------------")
        if role == "Codierer":
            print("Code: " + code)
        else:
            print("Code: XXXXX")
        print("")
        for item1, item2 in output:
            print(item1, "|", item2)
        print("--------------------------------------------------")

    def prompt_for_role(self) -> Role:
        while True:
            role = input("Wählen Sie eine Rolle 'Codierer' oder 'Rater': ").lower()
            if self.__check_for_ui_command(role):
                return self.prompt_for_role()
            if role == 'rater':
                return Role.DECODER
            elif role == 'codierer':
                return Role.ENCODER
            else:
                print("Ungültige Eingabe. Wählen Sie eine Rolle 'Codierer' oder 'Rater': ")

    def prompt_for_network_encoder(self) -> bool:
        while True:
            mode = input("Lokal oder Netzwerk: ").lower()
            if self.__check_for_ui_command(mode):
                return self.prompt_for_network_encoder()
            if mode == 'lokal':
                return False
            elif mode == 'netzwerk':
                return True
            else:
                print("Ungültige Eingabe. Wählen Sie eine Rolle 'Lokal' oder 'Netzwerk': ")

    def prompt_for_computer_decoder(self) -> bool:
        while True:
            role = input("Möchten Sie selbst raten oder soll der Computer raten? 'Selbst', 'Computer': ").lower()
            if self.__check_for_ui_command(role):
                return self.prompt_for_computer_decoder()
            if role == 'selbst':
                return False
            elif role == 'computer':
                return True
            else:
                print("Ungültige Eingabe. Wählen Sie 'Selbst' oder 'Computer': ")

    def prompt_for_host_addr(self) -> str:
        while True:
            connection = input("IP und Port? ")
            if self.__check_for_ui_command(connection):
                return self.prompt_for_host_addr()
            match = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}$', connection)
            if match:
                return connection
            else:
                print("Ungültige Eingabe. Bitte geben Sie eine gültige Adresse ein.")

    def prompt_for_code_length(self) -> int:
        while True:
            try:
                user_input = input("Bitte Code Länge wählen (4 oder 5): ")
                if self.__check_for_ui_command(user_input):
                    return self.prompt_for_code_length()
                code_length = int(user_input)
                if code_length in (4, 5):
                    return code_length
                else:
                    print("Ungültige Eingabe. Bitte wählen Sie 4 oder 5.")
            except ValueError:
                print("Ungültige Eingabe. Bitte wählen sie '4' oder '5'.")

    def prompt_for_number_of_colors(self) -> int:
        while True:
            try:
                user_input = input("Anzahl der Farben wählen, 2 bis 8 möglich: ")
                if self.__check_for_ui_command(user_input):
                    return self.prompt_for_number_of_colors()
                number_of_colors = int(user_input)
                if 2 <= number_of_colors <= 8:
                    return number_of_colors
                else:
                    print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 2 und 8.")
            except ValueError:
                print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 2 und 8.")

    def prompt_for_code(self, code_length: int, number_of_colors: int) -> Code:
        color_help = ", ".join(f"{color.name}:{color.value}" for color in list(Color)[:number_of_colors])
        color_check = "".join(str(color.value) for color in list(Color)[:number_of_colors])
        print(color_help)
        code = None
        while True:
            try:
                code = input("Bitte gebe einen Code ein: ")
                if self.__check_for_ui_command(code):
                    return self.prompt_for_code(code_length, number_of_colors)
                if not all(char in color_check for char in code) | len(code) > code_length:
                    print("Ungültige Eingabe. Bitte geben Sie einen Code aus den verfügbaren Farben ein")
                else:
                    break
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie einen Code aus den verfügbaren Farben ein")
        print(f"Dieser Code wurde gesetzt:  {code}")
        colors = []
        for char in code:
            colors.append(Color(int(char)))
        return Code(colors)

    def prompt_for_guess(self, code_length: int, number_of_colors: int) -> Code:
        color_help = ", ".join(f"{color.name}:{color.value}" for color in list(Color)[:number_of_colors])
        color_check = "".join(str(color.value) for color in list(Color)[:number_of_colors])
        print(color_help)
        guess = None
        while True:
            try:
                guess = input("Bitte gebe eine Frage ein: ")
                if self.__check_for_ui_command(guess):
                    return self.prompt_for_guess(code_length, number_of_colors)
                if not all(char in color_check for char in guess) | len(guess) != code_length:
                    print("Ungültige Eingabe. Bitte geben Sie eine Frage aus den verfügbaren Farben ein")
                else:
                    break
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Frage aus den verfügbaren Farben ein")
        print(f"Diese Frage wurde eingegeben:  {guess}")
        colors = []
        for char in guess:
            colors.append(Color(int(char)))
        return Code(colors)

    def prompt_for_rating(self, code_length: int) -> Rating:
        color_help = ["Weiss=7", "Schwarz=8"]
        print(color_help)
        while True:
            try:
                rating = input("Rating: ")
                if self.__check_for_ui_command(rating):
                    return self.prompt_for_rating(code_length)
                if not all(char in '78' for char in rating) | len(rating) > code_length:
                    print("Ungültige Eingabe. Bitte geben Sie ein leeres Rating oder ein Rating aus 7/8 ein")
                else:
                    break
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie die 7, 8 oder Nichts")
        print(f"Diese Feedback wurde gegeben:  {rating}")
        colors = []
        for char in rating:
            colors.append(Color(int(char)))
        return Rating(colors)
