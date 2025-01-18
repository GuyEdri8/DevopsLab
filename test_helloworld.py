import unittest
from helloworld import print_message
from io import StringIO
import sys

class TestHelloWorld(unittest.TestCase):
    def test_print_message(self):
        # Redirect stdout to capture the output of print_message
        captured_output = StringIO()
        sys.stdout = captured_output
        print_message()
        sys.stdout = sys.__stdout__

        # Verify the output
        self.assertEqual(captured_output.getvalue().strip(), "Hello World! from DevOps Lab")

if __name__ == "__main__":
    unittest.main()
