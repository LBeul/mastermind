from superhirn.logic.connector.data_controller_interface import DataControllerInterface
from superhirn.logic.connector.ui_controller_interface import UiControllerInterface
from superhirn.logic.encoder.encoder_interface import EncoderInterface
from superhirn.logic.util.code import Code
from superhirn.logic.util.rating import Rating


class HumanEncoder(EncoderInterface):
    def __init__(self, ui: UiControllerInterface):
        self._ui = ui
        self._generated_code = None

    def generate_code(self) -> Code:
        code = self._ui.prompt_for_code(self._game_data.get_code_length(), self._game_data.get_number_of_colors())
        return code

    def rate(self, code_guess: Code) -> Rating:
        rating = self._ui.prompt_for_rating(code_guess.get_length())
        return rating
