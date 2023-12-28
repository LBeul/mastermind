import unittest

from superhirn.logic.gamecontroller.game_controller import color_string_to_list
from superhirn.logic.util.color import Color


class GameControllerTestCase(unittest.TestCase):
    def test_color_list_conversion(self):
        values: list[Color] = color_string_to_list("1,2,3,4")
        self.assertCountEqual(values, [Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE])
