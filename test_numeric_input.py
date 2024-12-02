import pytest
from money import transfer_money, select_transaction
from person import Person


@pytest.fixture
def mock_person():
    return Person('Test', 'password', 50.00)


@pytest.fixture
def mock_functions(monkeypatch):
    def dummy_read_float(prompt, minimum, maximum):
        if 'Einzahlung' in prompt:
            return 20.00
        elif 'Auszahlung' in prompt:
            return 10.00

    monkeypatch.setattr('numeric_input.read_float', dummy_read_float)


def test_select_transaction_deposit(monkeypatch):
    inputs = iter(['E'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_transaction() == 'E'


def test_select_transaction_withdraw(monkeypatch):
    inputs = iter(['A'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_transaction() == 'A'


def test_select_transaction_exit(monkeypatch):
    inputs = iter(['Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_transaction() == 'Z'


def test_select_transaction_invalid(monkeypatch):
    inputs = iter(['X', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_transaction() == 'Z'
