import pytest
import main


test1 = [(number, number % 2 == 0) for number in range(1, 10)]

@pytest.mark.parametrize("number, expected", test1)
def test_is_even(number, expected):
    assert main.is_even(number) == expected

####################################################################################

test2 = [(n, n + 1, n * (n + 1)) for n in range(1, 10)]

@pytest.mark.parametrize("a, b, expected", test2)
def test_calculate_area(a, b, expected):
    assert main.calculate_area(a, b) == expected

####################################################################################

test3 = [(1, 1, 1, 'equilateral'),
         (1, 2, 1, 'isosceles'),
         (1, 2, 3, 'versatile'),
         (1, 1, 1, 'versatile')]

@pytest.mark.parametrize("a, b, c, expected", test3)
def test_classify_triangle(a, b, c, expected):
    assert main.classify_triangle(a, b, c) == expected