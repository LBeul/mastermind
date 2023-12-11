from superhirn.logic.encoder.encoder_interface import EncoderInterface


class LocalEncoder(EncoderInterface):
    def __init__(self, code_length, available_colors):
        self._code_length = code_length
        self._available_colors = available_colors
        self._generated_code = None

    def generate_code(self):
        pass

    def rate(self, code_guess):
        pass
