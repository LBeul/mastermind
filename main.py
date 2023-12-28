from superhirn.logic.gamecontroller.game_controller import GameController
from superhirn.view.client import Client

if __name__ == '__main__':
    controller = GameController()
    ui = Client()
    controller.setup(ui)
