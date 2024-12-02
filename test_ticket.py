import pytest
from ticket import Ticket

def test_joker_getter():
    ticket = Ticket(joker=123, numbers=[1, 2, 3, 4, 5])
    assert ticket.joker == 123

def test_joker_setter_valid():
    ticket = Ticket(joker=123, numbers=[1, 2, 3, 4, 5])
    ticket.joker = 456
    assert ticket.joker == 456

def test_joker_setter_invalid():
    ticket = Ticket(joker=123, numbers=[1, 2, 3, 4, 5])
    with pytest.raises(ValueError):
        ticket.joker = 'invalid'
    assert ticket.joker == 0

def test_numbers_getter():
    ticket = Ticket(joker=123, numbers=[1, 2, 3, 4, 5])
    assert ticket.numbers == [1, 2, 3, 4, 5]

def test_numbers_setter():
    ticket = Ticket(joker=123, numbers=[1, 2, 3, 4, 5])
    ticket.numbers = [6, 7, 8, 9, 10]
    assert ticket.numbers == [6, 7, 8, 9, 10]