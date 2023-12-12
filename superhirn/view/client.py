import os
import re
import time

from superhirn.view.game_view import GameView
from superhirn.view.main_menu_view import MainMenuView
from superhirn.view.manual_view import ManualView


class Client:
    def __init__(self):
        self.game_running = True
        self.role = None
        self.code_length = None
        self.color_amount = None
        self.code = None

    def command_loop(self):
        """
        Command loop for the user.
        """
        main_menu_view = MainMenuView()
        manual_view = ManualView()
        self.clear_screen()
        main_menu_view.print_start_menu()
        while self.game_running:
            user_input = input("Befehl eingeben: ")
            if user_input == 'help':
                self.clear_screen()
                manual_view.print_manual()
                main_menu_view.print_main_menu()
            elif user_input == 'start':
                self.clear_screen()
                main_menu_view.print_main_menu()
                self.setup_game()
                print("Spiel startet...")
                time.sleep(5)
                self.active_game_loop()
                break  # temp for prototype
            elif user_input == 'exit':
                print("Das Spiel wird beendet.")
                break
            else:
                print("Ungültiger Befehl.")

    def active_game_loop(self):
        """
        Game Example for Prototype.
        """
        game_view = GameView
        self.clear_screen()
        game_view.print_game_board([], [], self.role, self.code)
        time.sleep(3)
        self.clear_screen()
        game_view.print_game_board(["1111"], [""], self.role, self.code)
        time.sleep(3)
        self.clear_screen()
        game_view.print_game_board(["1111", "1112"], ["", "7"], self.role, self.code)
        time.sleep(3)
        self.clear_screen()
        game_view.print_game_board(["1111", "1112", "1121"], ["", "7", "8"], self.role, self.code)
        time.sleep(3)
        self.clear_screen()
        game_view.print_game_board(["1111", "1112", "1121", "1221"], ["", "7", "8", "8"], self.role, self.code)

    def setup_game(self):
        """
        Asks the user for game parameters.
        """
        game_view = GameView
        self.role = self.prompt_for_role()
        if self.role == "Rater":
            if self.prompt_for_encoder_mode() == "Netzwerk":
                self.prompt_for_connection()
        self.prompt_for_code_length()
        self.prompt_for_color_amount()
        if self.role == "Codierer":
            code = self.prompt_for_code(self.code_length, self.color_amount)

    def prompt_for_role(self) -> str:
        """
        Prompts the user to select a role.

        :return: selected role.
        """
        while True:
            role = input("Wählen Sie eine Rolle 'Codierer' oder 'Rater': ").lower()
            if role == 'rater':
                return 'Rater'
            elif role == 'codierer':
                return 'Codierer'
            else:
                print("Ungültige Eingabe. Wählen Sie eine Rolle 'Codierer' oder 'Rater': ")

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

    def clear_screen(self):
        """
        Cleans the terminal screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
