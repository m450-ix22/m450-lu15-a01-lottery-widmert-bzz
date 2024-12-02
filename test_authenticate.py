import pytest
from authenticate import login, load_people
from person import Person

@pytest.fixture
def mock_people(monkeypatch):
    people = [
        Person('Inga', 'geheim', 14.00),
        Person('Peter', 'secrät', 7.00),
        Person('Beatrice', 'passWORT', 23.00)
    ]
    monkeypatch.setattr('authenticate.load_people', lambda: people)
    return people

def test_login_with_correct_password(monkeypatch, mock_people):
    inputs = iter(['geheim'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    person = login()
    assert person.givenname == 'Inga'

def test_login_with_incorrect_password(monkeypatch, mock_people, capsys):
    inputs = iter(['wrong', 'geheim'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    person = login()
    captured = capsys.readouterr()
    assert 'Passwort falsch' in captured.out
    assert person.givenname == 'Inga'

def test_load_people_returns_correct_list():
    people = load_people()
    assert len(people) == 3
    assert people[0].givenname == 'Inga'
    assert people[1].givenname == 'Peter'
    assert people[2].givenname == 'Beatrice'