import os
import sys
import unittest


os.chdir("../")
sys.path[0] = os.getcwd()


import package_name


class UtilitsTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_(self):
        self.assertEqual(arg, arg2)

    def test_1(self):
        self.assertFalse(arg)



if __name__ == "__main__":
    unittest.main()