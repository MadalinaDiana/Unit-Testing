import pytest
from mock import patch
from code_for_unit_test import Cont


@pytest.fixture
def cont():
    user = Cont(1334456778, 'Madalina', 555.3)
    return user


@patch('builtins.print')
def test_display(mock_print, cont):
    cont.display_sold()
    mock_print.assert_called_with(
        f'The Holder {cont.holder_cont} of the account {cont.iban} has the balance {cont.balance}')


def test_debit(cont):
    cont.debit_cont(100)
    assert cont.balance == 655.3


def test_credit(cont):
    cont.credit_cont(400)
    assert cont.balance == 155.29999999999995
