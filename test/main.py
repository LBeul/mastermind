import unittest
from unittest import TestSuite

from test.data.test_data_models import TestSimple
from test.logic.decoder.test_local_decoder import LocalDecoder4PegsTestCase, LocalDecoder5PegsTestCase, \
    LocalDecoderRateGuess2, LocalDecoderRateGuess, LocalDecoderFilterPossibleCodes, LocalDecoderInitTestPossibleCodes3, \
    LocalDecoderInitTestPossibleCodes2, LocalDecoderInitTestPossibleCodes
from test.logic.encoder.test_local_encoder import LocalEncoderTestCase
from test.view.test_client import ClientTest

suite_client = unittest.TestLoader().loadTestsFromTestCase(ClientTest)
suite_local_decoder = unittest.TestLoader().loadTestsFromTestCase(LocalEncoderTestCase)
suite_data = unittest.TestLoader().loadTestsFromTestCase(TestSimple)
suite_local_encoder_1 = unittest.TestLoader().loadTestsFromTestCase(LocalDecoder4PegsTestCase)
suite_local_encoder_2 = unittest.TestLoader().loadTestsFromTestCase(LocalDecoder5PegsTestCase)
suite_local_encoder_3 = unittest.TestLoader().loadTestsFromTestCase(LocalDecoderRateGuess2)
suite_local_encoder_4 = unittest.TestLoader().loadTestsFromTestCase(LocalDecoderRateGuess)
suite_local_encoder_5 = unittest.TestLoader().loadTestsFromTestCase(LocalDecoderFilterPossibleCodes)
suite_local_encoder_6 = unittest.TestLoader().loadTestsFromTestCase(LocalDecoderInitTestPossibleCodes3)
suite_local_encoder_7 = unittest.TestLoader().loadTestsFromTestCase(LocalDecoderInitTestPossibleCodes2)
suite_local_encoder_8 = unittest.TestLoader().loadTestsFromTestCase(LocalDecoderInitTestPossibleCodes)
suite_local_encoder = TestSuite(
    [suite_local_encoder_1, suite_local_encoder_2, suite_local_encoder_3, suite_local_encoder_4, suite_local_encoder_5,
     suite_local_encoder_6, suite_local_encoder_7, suite_local_encoder_8])

suite_logic = TestSuite([suite_local_decoder, suite_local_encoder])
suite_complete = unittest.TestSuite([suite_client, suite_logic, suite_data])

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(
        suite_complete
    )
