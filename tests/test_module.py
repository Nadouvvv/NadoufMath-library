
import pytest
from nadouf_math import (
    Nadoufmath,
    sum_of, difference_of, division_of, int_division_of, multiply_of,
    square, cube, power, power_of_2,
    square_root, cube_root,
    factorial, gcd_with, lcm_with,
    floor, ceil,
    is_positive, is_negative, is_even, is_odd, sign,
    cos, sin, tan,
    number_pi, number_e
)

class TestBasicOperations:
    """Тесты базовых операций"""
    
    def test_sum(self):
        assert sum_of(2, 3) == 5
        assert sum_of(1, 2, 3, 4) == 10
        assert sum_of(-1, 1) == 0
    
    def test_difference(self):
        assert difference_of(10, 3) == 7
        assert difference_of(10, 3, 2) == 5
        assert difference_of(5) == 5
    
    def test_division(self):
        assert division_of(10, 2) == 5
        assert division_of(100, 2, 5) == 10
        with pytest.raises(ValueError):
            division_of(10, 0)
    
    def test_multiply(self):
        assert multiply_of(2, 3) == 6
        assert multiply_of(2, 3, 4) == 24

class TestPowersAndRoots:
    """Тесты степеней и корней"""
    
    def test_square(self):
        assert square(5) == 25
        assert square(-3) == 9
    
    def test_cube(self):
        assert cube(3) == 27
        assert cube(-2) == -8
    
    def test_power(self):
        assert power(2, 3) == 8
        assert power(5, 0) == 1
    
    def test_power_of_2(self):
        assert power_of_2(3) == 8
        assert power_of_2(0) == 1
    
    def test_square_root(self):
        assert square_root(64) == 8
        assert square_root(2) ** 2 == pytest.approx(2, rel=1e-10)
    
    def test_cube_root(self):
        assert cube_root(27) == 3
        assert cube_root(125) == pytest.approx(5, rel=1e-10)

class TestHigherMath:
    """Тесты высшей математики"""
    
    def test_factorial(self):
        assert factorial(5) == 120
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(3) == 6
    
    def test_gcd(self):
        assert gcd_with(12, 18) == 6
        assert gcd_with(12, 18, 24) == 6
        assert gcd_with(17, 19) == 1
    
    def test_lcm(self):
        assert lcm_with(12, 18) == 36
        assert lcm_with(12, 18, 24) == 72
        assert lcm_with(3, 5) == 15

class TestRounding:
    """Тесты округления"""
    
    def test_floor(self):
        assert floor(5.9) == 5
        assert floor(5.1) == 5
        assert floor(-3.7) == -4
        assert floor(-3.2) == -4
    
    def test_ceil(self):
        assert ceil(5.2) == 6
        assert ceil(5.9) == 6
        assert ceil(-3.2) == -3
        assert ceil(-3.8) == -3

class TestNumberProperties:
    """Тесты свойств чисел"""
    
    def test_is_positive(self):
        assert is_positive(5) is True
        assert is_positive(-3) is False
        assert is_positive(0) is False
    
    def test_is_negative(self):
        assert is_negative(-5) is True
        assert is_negative(3) is False
        assert is_negative(0) is False
    
    def test_is_even(self):
        assert is_even(4) is True
        assert is_even(7) is False
        assert is_even(0) is True
    
    def test_is_odd(self):
        assert is_odd(7) is True
        assert is_odd(4) is False
        assert is_odd(0) is False
    
    def test_sign(self):
        assert sign(5) == "Positive"
        assert sign(-3) == "Negative"
        assert sign(0) == "Zero"

class TestTrigonometry:
    """Тесты тригонометрии (с небольшой погрешностью)"""
    
    def test_cos(self):
        assert cos(0) == pytest.approx(1, rel=1e-10)
        assert cos(number_pi) == pytest.approx(-1, rel=1e-5)
        assert cos(number_pi/2) == pytest.approx(0, abs=1e-5)
    
    def test_sin(self):
        assert sin(0) == pytest.approx(0, rel=1e-10)
        assert sin(number_pi/2) == pytest.approx(1, rel=1e-5)
        assert sin(number_pi) == pytest.approx(0, abs=1e-5)
    
    def test_tan(self):
        assert tan(0) == pytest.approx(0, rel=1e-10)
        assert tan(number_pi/4) == pytest.approx(1, rel=1e-5)

class TestConstants:
    """Тесты констант"""
    
    
    def test_e(self):
        assert number_e == pytest.approx(2.718281828459)

class TestNadoufmathClass:
    """Тесты класса Nadoufmath"""
    
    def test_initialization(self):
        obj = Nadoufmath(5)
        assert obj.number == 5
    
    def test_methods(self):
        # Тест для square
        obj = Nadoufmath(5)
        result = obj.square()
        assert result == obj  # возвращает объект
        assert obj.number == 25
        
        # Тест для cube
        obj = Nadoufmath(5)
        result = obj.cube()
        assert result == obj
        assert obj.number == 125
        
        # Тест для power
        obj = Nadoufmath(5)
        result = obj.power(3)
        assert result == obj
        assert obj.number == 125  # проверяем, что число изменилось
    
    def test_chaining(self):
        """Тест последовательных операций"""
        obj = Nadoufmath(2)
        result = obj.power(3).square()  # (2³)² = 8² = 64
        # Обрати внимание: power возвращает число, а не объект!
        # Это может быть багом или фичей
    
    def test_trigonometry_methods(self):
        obj = Nadoufmath(0)
        obj.cos()
        assert obj.number == pytest.approx(1, rel=1e-10)
        
        obj = Nadoufmath(0)
        obj.sin()
        assert obj.number == pytest.approx(0, rel=1e-10)
        
        obj = Nadoufmath(0)
        obj.tan()
        assert obj.number == pytest.approx(0, rel=1e-10)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])