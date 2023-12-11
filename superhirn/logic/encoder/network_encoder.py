from superhirn.data.color import Color
from superhirn.logic.encoder.encoder_interface import EncoderInterface


class NetworkEncoder(EncoderInterface):
    def __init__(self, code_length: int, available_colors: list[Color], ip: str, port: int):
        self._code_length = code_length
        self._available_colors = available_colors
        self._ip_address = ip
        self._port = port
        self._generated_code = None

    def generate_code(self):
        pass

    def rate(self, code_guess):
        pass
