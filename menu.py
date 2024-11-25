def show_menu():
    """
    shows the main menu
    :return:
    """
    print('Lotto')
    print('---------')
    print('A) Konto Ein- und Auszahlungen tätigen')
    print('B) Lottotipps abgeben')
    print('Z) Beenden')


def select_menu():
    """
    asks the user to select a menu option
    :return: the selected option
    """
    show_menu()
    selection = ''
    while selection == '':
        user_input = input('Ihre Wahl > ')
        if user_input in ['A', 'B', 'Z']:
            selection = user_input
        else:
            print('Bitte geben Sie eine gültige Wahl ein')

    return selection

if __name__ == '__main__':
    pass