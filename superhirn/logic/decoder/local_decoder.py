from superhirn.logic.decoder.decoder_interface import DecoderInterface


class LocalDecoder(DecoderInterface):
    def __init__(self, code_length, available_colors):
        self._code_length = code_length
        self._available_colors = available_colors
        self._generated_code = None

    def guess(self):
        pass
