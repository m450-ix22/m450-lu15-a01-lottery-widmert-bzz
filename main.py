from authenticate import login
from lottery import create_ticket
from menu import select_menu
from money import transfer_money


def main():
    person = login()
    item = ''
    while item != 'Z':
        item = select_menu()
        if item == 'A':
            transfer_money(person)
        elif item == 'B':
            create_ticket(person)


if __name__ == '__main__':
    main()
