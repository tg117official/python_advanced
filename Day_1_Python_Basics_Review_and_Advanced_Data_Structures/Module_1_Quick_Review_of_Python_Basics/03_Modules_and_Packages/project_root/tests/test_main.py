# Unit test for main.py
import unittest
from project_package.utils import utility_function
from project_package.sub_package.sub_utils import helper_function
from project_package.sub_package.nested import nested_function

class TestMain(unittest.TestCase):
    def test_utils(self):
        self.assertIsNone(utility_function())

    def test_sub_utils(self):
        self.assertIsNone(helper_function())

    def test_nested(self):
        self.assertIsNone(nested_function())

if __name__ == "__main__":
    unittest.main()

