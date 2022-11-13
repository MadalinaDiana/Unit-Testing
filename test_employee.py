import pytest
from mock import patch
from code_for_unit_test import Employee


@pytest.fixture
def employee():
    em = Employee('Mada', 'Diana', 1780)
    return em


@patch('builtins.print')
def test_describe(mock_print, employee):
    employee.describe()
    mock_print.assert_called_with(
        f'Name of the employee is {employee.complet_name()} and has the salary on month {employee.salary_month()}.')


def test_month_salary(employee):
    assert employee.salary_month() == 1780


def test_annual_salary(employee):
    assert employee.salary_annual() == 21360


def test_salary(employee):
    salary_before = employee.salary
    employee.salary_marriage(30)
    assert employee.salary == salary_before + (salary_before * 30/100)
