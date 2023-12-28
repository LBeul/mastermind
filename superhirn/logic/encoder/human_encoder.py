from superhirn.logic import color_string_to_list
from superhirn.logic.connector.ui_controller_interface import UiControllerInterface
from superhirn.logic.encoder.encoder_interface import EncoderInterface
from superhirn.logic.util.code import Code
from superhirn.logic.util.rating import Rating


class HumanEncoder(EncoderInterface):
    def __init__(self, ui: UiControllerInterface):
        self._ui = ui
        self._generated_code = None

    def generate_code(self, code_length: int, color_availabilities: int) -> Code:
        input_string = self._ui.prompt_for_code(code_length, color_availabilities)
        color_list = color_string_to_list(input_string)
        return Code(color_list)

    def rate(self, code_guess: Code) -> Rating:
        input_string = self._ui.prompt_for_rating(len(code_guess.to_int_list()))
        color_list = color_string_to_list(input_string)
        return Rating(color_list)
