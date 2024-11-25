def read_int(prompt, minimum, maximum):
    """
    reads and validates an integer
    :param prompt: the input prompt
    :param minimum: the smallest number allowed
    :param maximum: the largest number allowed
    :return: valid input
    """
    number = None
    while number is None:
        try:
            number = int(input(prompt))
            if number < minimum or number > maximum:
                print('Eingabe ist zu gross oder zu klein')
                number = None
        except ValueError:
            print('Geben Sie eine Ganzzahl ein')

    return number


def read_float(prompt, minimum, maximum):
    """
    reads and validates a floating point number
    :param prompt: the input prompt
    :param minimum: the smallest number allowed
    :param maximum: the largest number allowed
    :return: valid input
    """
    number = None
    while number is None:
        try:
            number = float(input(prompt))
            if number < minimum or number > maximum:
                print('Eingabe ist zu gross oder zu klein')
                number = None
        except ValueError:
            print('Geben Sie eine Zahl ein')

    return number


if __name__ == '__main__':
    pass
