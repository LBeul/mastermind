import unittest

from superhirn.data.game import Game
from superhirn.logic.util.code import Code
from superhirn.logic.util.color import Color
from superhirn.logic.util.rating import Rating


class TestSimple(unittest.TestCase):

    def test_get_color_at(self):
        code = Code([Color.RED])
        self.assertEqual(code.get_color_at(0), Color.RED)

    def test_add_question(self):
        game = Game()
        game.add_question(given_question=Code(colors=[Color.RED, Color.WHITE, Color.BLACK, Color.BLUE,
                                                      Color.RED, Color.WHITE, Color.BLACK, Color.BLUE]))
        self.assertIsNotNone(game.questions)

    def test_add_rating(self):
        game = Game()
        rating = Rating(([Color.WHITE, Color.BLACK, Color.WHITE, Color.BLACK, Color.WHITE]))
        game.add_rating(given_rating=rating)
        self.assertIsNotNone(game.ratings)

#  def test_count_white(self):
#     code = [Color.WHITE, Color.BLACK, Color.WHITE, Color.BLACK, Color.WHITE]
#     rating = Rating(code)
#    count = rating.count_white()
#   self.assertEqual(3, count)
