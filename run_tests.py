import unittest

# Import test cases from different test files
from test_text_processing import TestTextProcessing
from test_vectorization import TestVectorization
from test_grpc_api import TestGRPCAPI
from test_containerization import TestContainerization

# Create a test suite
suite = unittest.TestSuite()
suite.addTests([
    unittest.TestLoader().loadTestsFromTestCase(TestTextProcessing),
    unittest.TestLoader().loadTestsFromTestCase(TestVectorization),
    unittest.TestLoader().loadTestsFromTestCase(TestGRPCAPI),
    unittest.TestLoader().loadTestsFromTestCase(TestContainerization)
])

# Run the test suite
runner = unittest.TextTestRunner()
runner.run(suite)