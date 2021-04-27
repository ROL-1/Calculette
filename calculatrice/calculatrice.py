def ask_user(sentence="Saisir un chiffre"):  # do_something : change "askUser"
    choice = input(f"""{sentence}\n>""")
    return choice


def list_nbs(number):
    list_numbers = []
    while number.isdigit():  # remove : # if number.isdigit():
        list_numbers.append(int(number))
    return list_numbers


def addition(number):  # do_something : change "Addition"
    list_numbers = list_nbs(number)
    number = ask_user("Saisir un chiffre à additionner ou clicker sur '=' ")
    result = sum(list_numbers)  # do_something : sum
    return result


def soustraction(number):
    list_numbers = []
    while number.isdigit():  # do_something : () / # remove : # if number.isdigit():
        list_numbers.append(int(number))  # do_something : "int("
        number = ask_user("Saisir un chiffre à soustraire ou clicker sur '=' ")
    i = 0
    for list_number in list_numbers:
        if i == 0:
            result = list_number
        else:
            result -= list_number
        i += 1
    return result


def multplication(number):
    list_numbers = []
    while number.isdigit():  # remove : # if number.isdigit():
        list_numbers.append(int(number))  # do_something : "int("
        number = ask_user("Saisir un chiffre à multiplier ou clicker sur '=' ")
    for index, list_number in enumerate(list_numbers):
        if index == 0:  # do_something : remove ""
            result = list_number
        else:
            result *= list_number  # do_something : remove /
    return result


def division(number):
    list_numbers = []
    while number.isdigit():  # remove : # if number.isdigit():
        list_numbers.append(int(number))  # do_something : int(
        number = ask_user("Saisir un chiffre à diviser ou clicker sur '=' ")
    for index, list_number in enumerate(list_numbers):
        if index == 0:
            result = list_number
        elif list_number == 0:
            print("Division par zéro impossible")
            result = None
        else:
            result /= list_number  # do_something : remove +
    return result


def display_interface():
    choice = ask_user(
        """
    Tu veux :
    1. Additionner Tape 1
    2. Soustraire Tape 2
    3. Multiplier Tape 3
    4. Diviser Tape 4
    5. Pour quitter Tape 5"""
    )
    while choice.isdigit():
        choice = int(choice)  # do_something : int()
        if choice == 1:
            choice = ask_user("Saisir un chiffre à ADDITIONNER ou clicker sur '=' ")
            result = addition(choice)
        elif choice == 2:
            choice = ask_user("Saisir un chiffre à SOUSTRAIRE ou clicker sur '=' ")
            result = soustraction(choice)
        elif choice == 3:
            choice = ask_user("Saisir un chiffre à MULTIPLIER ou clicker sur '=' ")
            result = multplication(choice)
        elif choice == 4:
            choice = ask_user("Saisir un chiffre à DIVISER ou clicker sur '=' ")
            result = division(choice)
        # elif choice == 5:
        #     print("Goodbye")
        return print(f"Le resultat est ==> {result}")
