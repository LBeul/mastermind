import unittest
from unittest.mock import patch

from superhirn.view.client import Client


class ClientTest(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls):
        cls.client = Client()

    @classmethod
    def tearDownClass(cls):
        cls.client = None

    @patch('builtins.input', side_effect=['Codierer'])
    def test_prompt_for_role_good_1(self, mock_input):
        """
        Test prompt_for_role with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_role()
        self.assertEqual(result, 'Codierer')

    @patch('builtins.input', side_effect=['Rater'])
    def test_prompt_for_role_good_2(self, mock_input):
        """
        Test prompt_for_role with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_role()
        self.assertEqual(result, 'Rater')

    @patch('builtins.input', side_effect=['Admin', 'Codierer'])
    def test_prompt_for_role_bad_1(self, mock_input):
        """
        Test prompt_for_role with invalid input than with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_role()
        self.assertEqual(result, 'Codierer')

    @patch('builtins.input', side_effect=['', 'Codierer'])
    def test_prompt_for_role_bad_2(self, mock_input):
        """
        Test prompt_for_role with invalid input than with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_role()
        self.assertEqual(result, 'Codierer')

    @patch('builtins.input', side_effect=['Admin', 'Rater'])
    def test_prompt_for_role_bad_3(self, mock_input):
        """
        Test prompt_for_role with invalid input than with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_role()
        self.assertEqual(result, 'Rater')

    @patch('builtins.input', side_effect=['', 'Rater'])
    def test_prompt_for_role_bad_4(self, mock_input):
        """
        Test prompt_for_role with invalid input than with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_role()
        self.assertEqual(result, 'Rater')

    @patch('builtins.input', side_effect=['Netzwerk'])
    def test_prompt_for_encoder_mode_good_1(self, mock_input):
        """
        Test prompt_for_encoder with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_encoder_mode()
        self.assertEqual(result, 'Netzwerk')

    @patch('builtins.input', side_effect=['Lokal'])
    def test_prompt_for_encoder_mode_good_2(self, mock_input):
        """
        Test prompt_for_encoder with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_encoder_mode()
        self.assertEqual(result, 'Lokal')

    @patch('builtins.input', side_effect=['Network', 'Netzwerk'])
    def test_prompt_for_encoder_mode_bad_1(self, mock_input):
        """
        Test prompt_for_encoder with invalid input than with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_encoder_mode()
        self.assertEqual(result, 'Netzwerk')

    @patch('builtins.input', side_effect=['local', 'Lokal'])
    def test_prompt_for_encoder_mode_bad_2(self, mock_input):
        """
        Test prompt_for_encoder with invalid input than with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_encoder_mode()
        self.assertEqual(result, 'Lokal')

    @patch('builtins.input', side_effect=['', 'Netzwerk'])
    def test_prompt_for_encoder_mode_bad_3(self, mock_input):
        """
        Test prompt_for_encoder with invalid input than with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_encoder_mode()
        self.assertEqual(result, 'Netzwerk')

    @patch('builtins.input', side_effect=['', 'Lokal'])
    def test_prompt_for_encoder_mode_bad_4(self, mock_input):
        """
        Test prompt_for_encoder with invalid input than with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_encoder_mode()
        self.assertEqual(result, 'Lokal')

    @patch('builtins.input', side_effect=['127.0.0.1:8080'])
    def test_prompt_for_connection_good(self, mock_input):
        """
        Test prompt_for_connection with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_connection()
        self.assertEqual(result, '127.0.0.1:8080')

    @patch('builtins.input', side_effect=['MeinSpielNetwork', '127.0.0.1:8080'])
    def test_prompt_for_connection_bad_1(self, mock_input):
        """
        Test prompt_for_connection with invalid input than with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_connection()
        self.assertEqual(result, '127.0.0.1:8080')

    @patch('builtins.input', side_effect=['', '127.0.0.1:8080'])
    def test_prompt_for_connection_bad_2(self, mock_input):
        """
        Test prompt_for_connection with invalid input than with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_connection()
        self.assertEqual(result, '127.0.0.1:8080')

    @patch('builtins.input', side_effect=['4'])
    def test_prompt_for_code_length_good(self, mock_input):
        """
        Test prompt_for_code_length with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_code_length()
        self.assertEqual(result, 4)

    @patch('builtins.input', side_effect=['', '3', '23', '4'])
    def test_prompt_for_code_length_bad(self, mock_input):
        """
        Test prompt_for_code_length with invalid input than with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_code_length()
        self.assertEqual(result, 4)

    @patch('builtins.input', side_effect=['5'])
    def test_prompt_for_color_amount_good(self, mock_input):
        """
        Test prompt_for_color_amount with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_color_amount()
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect=['', '9', '20', '5'])
    def test_prompt_for_color_amount_bad(self, mock_input):
        """
        Test prompt_for_color_amount with invalid input than with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_color_amount()
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect=['1', '2', '3', '4'])
    def test_prompt_for_code_good(self, mock_input):
        """
        Test prompt_for_code with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_code(4, 8)
        self.assertEqual(result, [1, 2, 3, 4])

    @patch('builtins.input', side_effect=['', '1', '10', '2', '-2', '3', '4'])
    def test_prompt_for_code_bad(self, mock_input):
        """
        Test prompt_for_code with invalid input than with valid input
        :param mock_input:
        """
        result = self.client.prompt_for_code(4, 8)
        self.assertEqual(result, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
