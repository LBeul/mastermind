import unittest

from superhirn.data.code import Code
from superhirn.data.color import Color


class TestSimple(unittest.TestCase):

    def test_get_color_at(self):
        code = Code([Color.RED])
        self.assertEqual(code.get_color_at(0), Color.RED)

# if __name__ == '__main__':
