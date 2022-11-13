import pytest
from mock import patch
from code_for_unit_test import Rectangle


@pytest.fixture
def rectangle():
    dr = Rectangle(13, 6, 'blue')
    return dr


@patch('builtins.print')
def test_describe(mock_print, rectangle):
    rectangle.describe()
    mock_print.assert_called_with(
        f'The rectangle has {rectangle.lenght} lenght, {rectangle.width}  width and color {rectangle.color}. \n '
        f'has the perimeter {rectangle.perimeter()}, aria {rectangle.aria()}')


def test_aria(rectangle):
    assert rectangle.aria() == rectangle.lenght * rectangle.width


def test_perimeter(rectangle):
    assert rectangle.perimeter() == 2 * rectangle.aria()


def test_change_the_color(rectangle):
    rectangle.change_color('red')
    assert rectangle.color == 'red'
