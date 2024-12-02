import pytest
from unittest.mock import MagicMock
from lottery import create_ticket, select_numbers, print_ticket
from person import Person
from ticket import Ticket


# Fixtures
@pytest.fixture(scope="module")
def mock_person():
    return Person('Test', 'password', 50.00)


@pytest.fixture
def mock_ticket():
    return Ticket(0, [])


# Tests
def test_create_ticket_with_sufficient_balance(mock_person, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    create_ticket(mock_person)
    assert mock_person.balance == 48.00


def test_create_ticket_with_insufficient_balance(mock_person, monkeypatch):
    mock_person.balance = 1.00  # Set balance below ticket price
    monkeypatch.setattr('builtins.input', lambda _: '1')
    create_ticket(mock_person)
    assert mock_person.balance == 1.00  # Balance should remain unchanged


def test_select_numbers_valid_input(mock_ticket, monkeypatch):
    inputs = iter(['1', '2', '3', '4', '5', '6', '1'])  # Valid inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    select_numbers(mock_ticket)
    assert mock_ticket.numbers == [1, 2, 3, 4, 5, 6]
    assert mock_ticket.joker == 1


def test_select_numbers_duplicate_input(mock_ticket, monkeypatch):
    inputs = iter(['1', '1', '2', '3', '4', '5', '6', '1'])  # Simulate duplicates
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    select_numbers(mock_ticket)
    assert mock_ticket.numbers == [1, 2, 3, 4, 5, 6]
    assert mock_ticket.joker == 1


def test_print_ticket_output(mock_ticket):
    mock_ticket.numbers = [1, 2, 3, 4, 5, 6]
    mock_ticket.joker = 1

    # Use a MagicMock to capture print output
    mock_writer = MagicMock()
    print_ticket(mock_ticket, writer=mock_writer)

    # Validate that the output was written correctly
    mock_writer.assert_any_call("X [1, 2, 3, 4, 5, 6]")
    mock_writer.assert_any_call("Jokerzahl:  1")
