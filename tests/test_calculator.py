from calculator.calculator import Calculator

class TestCalculator:
    def test_div(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = round(cal.divide(a, b),2)

        # assert
        expected = 3.50
        assert result == expected
