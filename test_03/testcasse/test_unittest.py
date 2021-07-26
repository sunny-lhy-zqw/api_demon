import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
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
    @unittest.skipIf(1==1,"相等")
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

if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(demon01("test_demon01_case2"))
    # suite.addTest(demon02("test_demon02_case2"))
    # unittest.TextTestRunne r().run(suite)

    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demon02)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(demon01)
    # suiteall = unittest.TestSuite([suite2,suite1])
    # unittest.TextTestRunner().run(suiteall)
    # discover = unittest.defaultTestLoader.discover("./",pattern="test_*.py")
    # unittest.TextTestRunner().run(discover)
    # re_file = 'test_report_example.html'
    # re_title = 'test_example'
    # desc = 'my project'
    # with open(re_file, 'wb') as report:
    #     runner = HTMLTestRunner(stream=report,title=re_title,description=desc)
    #     runner.run(discover)
    pytest.main("-v -x  demon01")
