from superhirn.logic.encoder.encoder_interface import EncoderInterface


class NetworkEncoder(EncoderInterface):
    def __init__(self, code_length, available_colors):
        self._code_length = code_length
        self._available_colors = available_colors
        self._generated_code = None
        self._ip_address = None
        self._port = None

    def generate_code(self):
        pass

    def rate(self, code_guess):
        pass

    def set_network_config(self, ip, port):
        pass
