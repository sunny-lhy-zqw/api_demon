import pytest

from test_03.testcasse.test_pytest.test1 import Calc


class TestCalc():
    def test_add(self):
        self.calc = Calc()
        result = self.calc.add(12, 34)
        print(result)

    def test_div(self):
        self.calc=Calc()
        result = self.calc.div(12, 3)
        print(result)


if __name__ == '__main__':
    pytest.main(['-vs', 'test1.py::TestCalc::test_add'])
