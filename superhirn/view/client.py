import re

from superhirn.view.main_menu_view import MainMenuView
from superhirn.view.manual_view import ManualView


class Client:
    def __init__(self):
        self.is_game_running = False

    def start_game(self):
        """
        Command loop for the user.
        """
        main_menu_view = MainMenuView()
        manual_view = ManualView()

        main_menu_view.print_main_menu()
        while not self.is_game_running:
            user_input = input("Befehl eingeben: ")
            if user_input == 'help':
                manual_view.print_manual()
            elif user_input == 'start':
                if self.prompt_for_role() == "Rater":
                    if self.prompt_for_encoder_mode() == "Netzwerk":
                        self.prompt_for_connection()
                self.prompt_for_code_length()
                self.prompt_for_color_amount()
                self.prompt_for_code(4, 3)
                break
            elif user_input == 'exit':
                print("Das Spiel wird beendet.")
                break
            else:
                print("Ungültiger Befehl.")

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

        :return: selected code.
        """
        code_colors = []
        code = ""
        print("RED = 1,GREEN = 2, YELLOW = 3, BLUE = 4, ORANGE = 5, BROWN = 6, WHITE = 7,BLACK = 8")
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
        print(f"Der Code lautet:  {code}")
        return code
