import unittest

from superhirn.main import multiply


class TestSimple(unittest.TestCase):

    def test_multiply_normal(self):
        self.assertEqual(multiply(5, 6), 30)

    def test_multiply_zero(self):
        self.assertEqual(multiply(10, 0), 0)


if __name__ == '__main__':
    unittest.main()
