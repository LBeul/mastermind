import os
import re

from superhirn.logic.ui_connector.ui_connector_interface import UiControllerInterface
from superhirn.view.main_menu_view import MainMenuView
from superhirn.view.manual_view import ManualView


class Client(UiControllerInterface):

    def show_help(self):
        manual_view = ManualView()
        self.clear_screen()
        manual_view.print_manual()

    def show_menu(self) -> str:
        main_menu_view = MainMenuView()
        self.clear_screen()
        main_menu_view.print_main_menu()
        command = input().lower()
        if command == 'start':
            return "start"
        elif command == 'help':
            return "help"
        elif command == 'exit':
            return "exit"
        else:
            print("Ungültige Eingabe")
        return command

    def prompt_for_role(self) -> str:
        while True:
            role = input("Wählen Sie eine Rolle 'Codierer' oder 'Rater': ").lower()
            if role == 'rater':
                return 'Rater'
            elif role == 'codierer':
                return 'Codierer'
            else:
                print("Ungültige Eingabe. Wählen Sie eine Rolle 'Codierer' oder 'Rater': ")

    def prompt_for_decoder_mode(self) -> str:
        while True:
            role = input("Möchten Sie selbst raten oder soll der Computer raten? 'Selbst', 'Computer': ").lower()
            if role == 'selbst':
                return 'Selbst'
            elif role == 'computer':
                return 'Computer'
            else:
                print("Ungültige Eingabe. Wählen Sie 'Selbst' oder 'Computer': ")

    def prompt_for_encoder_mode(self) -> str:
        """
        Prompts the user to select the encoder type.

        :return: selected type.
        """
        while True:
            mode = input("Lokal oder Netzwerk: ").lower()
            if mode == 'lokal':
                return 'Lokal'
            elif mode == 'netzwerk':
                return 'Netzwerk'
            else:
                print("Ungültige Eingabe. Wählen Sie eine Rolle 'Lokal' oder 'Netzwerk': ")

    def prompt_for_connection(self) -> str:
        """
        Prompts the user to set the connection address.
        ip:port

        :return: selected role.
        """
        while True:
            connection = input("IP und Port? ")
            match = re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}$', connection)
            if match:
                return connection
            else:
                print("Ungültige Eingabe. Bitte geben Sie eine gültige Adresse ein.")

    def prompt_for_code_length(self) -> int:
        """
        Prompts the user to set the code length.
        4 or 5 is valid

        :return: selected length.
        """
        while True:
            try:
                code_length = int(input("Bitte Code Länge wählen (4 oder 5): "))
                if code_length in (4, 5):
                    self.code_length = code_length  # temp als Mock
                    return code_length
                else:
                    print("Ungültige Eingabe. Bitte wählen Sie 4 oder 5.")
            except ValueError:
                print("Ungültige Eingabe. Bitte wählen sie '4' oder '5'.")

    def prompt_for_color_amount(self) -> int:
        """
        Prompts the user to set the amount of colors.
        2 to 8 is valid

        :return: selected amount.
        """
        while True:
            try:
                color_amount = int(input("Anzahl der Farben wählen, 2 bis 8 möglich: "))
                if 2 <= color_amount <= 8:
                    self.color_amount = color_amount  # temp als Mock
                    return color_amount
                else:
                    print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 2 und 8.")
            except ValueError:
                print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 2 und 8.")

    def prompt_for_code(self, code_length: int, color_amount: int) -> str:
        """
        Prompts the user to set the code.
        Prints help for available_colors.

        :return: selected code.
        """
        color_help = ["Rot=1", "Grün=2", "Gelb=3", "Blau=4", "Orange=5", "Braun=6", "Weiss=7", "Schwarz=8"]
        available_colors = color_help[:color_amount]
        print(available_colors)
        code = ""
        for i in range(code_length):
            while True:
                try:
                    element = int(input(f"Farbe an Stelle {i + 1} von {code_length}: "))
                    if 1 <= element <= color_amount:
                        code = code + str(element)
                        break
                    else:
                        print(f"Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und {color_amount}.")
                except ValueError:
                    print(f"Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und {color_amount}.")
        print(f"Der Code wurde gesetzt:  {code}")
        self.code = code
        return code

    def prompt_for_guess(self, code_length: int, color_amount: int) -> str:
        color_help = ["Rot=1", "Grün=2", "Gelb=3", "Blau=4", "Orange=5", "Braun=6", "Weiss=7", "Schwarz=8"]
        available_colors = color_help[:color_amount]
        print(available_colors)
        guess = ""
        for i in range(code_length):
            while True:
                try:
                    element = int(input(f"Farbe an Stelle {i + 1} von {code_length}: "))
                    if 1 <= element <= color_amount:
                        guess = guess + str(element)
                        break
                    else:
                        print(f"Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und {color_amount}.")
                except ValueError:
                    print(f"Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und {color_amount}.")
        print(f"Der Code wurde geraten:  {guess}")
        return guess

    def prompt_for_rating(self, code_length: int) -> str:
        color_help = ["Weiss=7", "Schwarz=8"]
        print(color_help)
        while True:
            try:
                rating = input("Rating: ")
                if not all(char in '78' for char in rating) | len(rating) > code_length:
                    print("Ungültige Eingabe. Bitte geben Sie ein leeres Rating oder ein Rating aus 7/8 ein")
                else:
                    break
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie die 7, 8 oder Nichts")
        print(f"Diese Feedback wurde gegeben:  {rating}")
        return rating

    def clear_screen(self):
        """
        Cleans the terminal screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
