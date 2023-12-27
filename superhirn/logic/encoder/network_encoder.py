from superhirn.data.code import Code
from superhirn.logic.encoder.encoder_interface import EncoderInterface


class NetworkEncoder(EncoderInterface):
    def __init__(self, host: str):
        self._host = host
        self._generated_code = None

    def generate_code(self, code_length: int, color_availabilities: int) -> Code:
        pass

    def rate(self, code_guess):
        pass
