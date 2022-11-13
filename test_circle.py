import math

import pytest
from mock import patch
from code_for_unit_test import Circle


@pytest.fixture
def circle():
    cr = Circle(13, 'blue')
    return cr


@patch('builtins.print')
def test_describe(mock_print, circle):
    circle.describe()
    mock_print.assert_called_with(
        f'The arie of the circle is: {circle.aria()}, color of the circle is {circle.color} and have the diameter '
        f'{circle.diameter()} and the circumference {circle.circumference()}')


def test_aria(circle):
    assert circle.aria() == math.pi * circle.radius ** 2


def test_diameter(circle):
    assert circle.diameter() == 26


def test_circumference(circle):
    assert circle.circumference() == math.pi * circle.diameter()

