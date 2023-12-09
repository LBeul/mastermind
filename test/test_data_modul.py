import unittest

from superhirn.data.Code import Code
from superhirn.data.Color import Color


class TestSimple(unittest.TestCase):

    def test_get_color_at(self):
        Code([Color.RED])
        self.assertEqual(Code.get_color_at,0, Color.RED)

# if __name__ == '__main__':

