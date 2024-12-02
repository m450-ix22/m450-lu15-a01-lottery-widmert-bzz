import pytest

from person import Person


def test_givenname_getter():
    person = Person('Test', 'password', 50.00)
    assert person.givenname == 'Test'

def test_givenname_setter():
    person = Person('Test', 'password', 50.00)
    person.givenname = 'NewName'
    assert person.givenname == 'NewName'

def test_password_getter():
    person = Person('Test', 'password', 50.00)
    assert person.password == 'password'

def test_password_setter():
    person = Person('Test', 'password', 50.00)
    person.password = 'newpassword'
    assert person.password == 'newpassword'

def test_balance_getter():
    person = Person('Test', 'password', 50.00)
    assert person.balance == 50.00

def test_balance_setter():
    person = Person('Test', 'password', 50.00)
    person.balance = 100.00
    assert person.balance == 100.00

def test_balance_setter_invalid_value():
    person = Person('Test', 'password', 50.00)
    with pytest.raises(ValueError):
        person.balance = 'invalid'