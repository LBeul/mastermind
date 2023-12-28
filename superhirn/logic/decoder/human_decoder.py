from superhirn.logic import color_string_to_list
from superhirn.logic.connector.ui_controller_interface import UiControllerInterface
from superhirn.logic.decoder.decoder_interface import DecoderInterface
from superhirn.logic.util.code import Code


class HumanDecoder(DecoderInterface):
    def __init__(self, ui: UiControllerInterface, game_data: DataControllerInterface):
        self._ui = ui

    def guess(self) -> Code:
        print("Sie dürfen raten:")
        code = self._ui.prompt_for_guess(self._game_data.get_code_length(),
                                         self._game_data.get_number_of_colors())
        return code
