import pytest
from lottery import create_ticket, select_numbers
from ticket import Ticket


class MockPerson:
    """
    Mock-Klasse für die Simulation einer Person mit einem Guthaben.
    """

    def __init__(self, balance):
        self.balance = balance


def test_select_numbers(monkeypatch):
    """
    Testet die select_numbers-Funktion, um sicherzustellen, dass die Zahlen korrekt ausgewählt werden.
    """
    ticket = Ticket(0, [])
    inputs = iter([1, 2, 3, 4, 5, 6, 2])  # Erste 6 Zahlen sind Lottozahlen, letzte Zahl ist der Joker
    # Patchen Sie `read_int` in `lottery` statt in `numeric_input`
    monkeypatch.setattr('lottery.read_int', lambda *args, **kwargs: next(inputs))

    select_numbers(ticket)

    # Überprüfen, ob die ausgewählten Zahlen korrekt sind
    assert len(ticket.numbers) == 6
    assert set(ticket.numbers) == {1, 2, 3, 4, 5, 6}
    assert ticket.joker == 2


def test_create_ticket_with_sufficient_balance(monkeypatch):
    """
    Testet die create_ticket-Funktion, wenn genug Guthaben vorhanden ist.
    """
    person = MockPerson(10.00)
    inputs = iter([1, 2, 3, 4, 5, 6, 2])  # Eingaben für Zahlen und Joker
    monkeypatch.setattr('lottery.read_int', lambda *args, **kwargs: next(inputs))
    monkeypatch.setattr('lottery.print_ticket', lambda *args, **kwargs: None)  # Ticket-Druck deaktivieren

    create_ticket(person)

    # Überprüfen, ob das Guthaben korrekt reduziert wurde
    assert person.balance == 8.00


def test_create_ticket_with_insufficient_balance(monkeypatch, capsys):
    """
    Testet die create_ticket-Funktion, wenn nicht genug Guthaben vorhanden ist.
    """
    person = MockPerson(1.00)
    inputs = iter([1, 2, 3, 4, 5, 6, 2])  # Eingaben für Zahlen und Joker
    monkeypatch.setattr('lottery.read_int', lambda *args, **kwargs: next(inputs))
    monkeypatch.setattr('lottery.print_ticket', lambda *args, **kwargs: None)  # Ticket-Druck deaktivieren

    create_ticket(person)

    # Überprüfen, ob das Guthaben nicht verändert wurde
    assert person.balance == 1.00

    # Überprüfen, ob die richtige Nachricht ausgegeben wurde
    captured = capsys.readouterr()
    assert 'Zuwenig Guthaben' in captured.out
