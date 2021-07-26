import unittest

import pytest

class demon01(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup_class")
    def setUp(self) -> None:
        print("setup")
    def tearDown(self) -> None:
        print("teardown")
    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown_class")

    def test_demon01_case1(self):
        print("test_demon01_case1")
    def test_demon01_case2(self):
        print("test_demon01_case2")

class demon02(unittest.TestCase):
    def setUp(self) -> None:
        print("setup")
    def tearDown(self) -> None:
        print("teardown")
    def test_demon02_case1(self):
        print("test_demon02_case1")
    def test_demon02_case2(self):
        print("test_demon02_case2")

# if __name__ == '__main__':
#     unittest.main()
#     suite = unittest.TestSuite()
#     suite.addTest(demon01("test_demon01_case2"))
#     suite.addTest(demon02("test_demon02_case2"))
#     unittest.TextTestRunner().run(suite)

    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demon02)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(demon01)
    # suiteall = unittest.TestSuite([suite2,suite1])
    # unittest.TextTestRunner().run(suiteall)

