from superhirn.data.code import Code
from superhirn.logic import color_string_to_list
from superhirn.logic.decoder.decoder_interface import DecoderInterface
from superhirn.logic.ui_connector.ui_connector_interface import UiControllerInterface


class HumanDecoder(DecoderInterface):
    def __init__(self, ui: UiControllerInterface):
        self._attempts: list[Code] = []
        self._ui = ui

    def guess(self, code_length: int, color_availabilities: int) -> Code:
        input_string = self._ui.prompt_for_guess(code_length, color_availabilities)
        color_list = color_string_to_list(input_string)
        return Code(color_list)
