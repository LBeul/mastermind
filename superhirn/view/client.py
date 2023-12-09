import re


class Client:

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

    def prompt_for_code(self, code_length, color_amount) -> list:
        """
        Prompts the user to set the code.

        :return: selected code.
        """
        code_array = []
        for i in range(code_length):
            while True:
                try:
                    element = int(input(f"Farbe an Stelle {i + 1} von {code_length}: "))
                    if 1 <= element <= color_amount:
                        code_array.append(element)
                        break
                    else:
                        print(f"Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und {color_amount}.")
                except ValueError:
                    print(f"Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und {color_amount}.")
        print(f"Der Code lautet: {code_array}")
        return code_array
