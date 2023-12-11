from superhirn.logic.gamecontroller.game_controller_interface import GameControllerInterface
from superhirn.logic.game_states import GameStates


class GameController(GameControllerInterface):

    def __init__(self):
        self._game_state = GameStates.SETUP
        self._user_role = None
        self._is_online = None

    def get_instance(self):
        # TODO: Check how to implement singletons in python
        pass

    def start_game(self, user_role, is_online):
        self._game_state = GameStates.START
        self._user_role = user_role
        self._is_online = is_online
        pass

    def get_game_state(self):
        pass
