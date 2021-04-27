def ask_user(sentence="Saisir un chiffre"):  # do_something : change "askUser"
    choice = input(f"""{sentence}\n>""")
    return choice


def values(number):
    list_numbers = []
    while number.isdigit():
        list_numbers.append(int(number))
        number = ask_user("Saisir un chiffre ou clicker sur '=' ")
    return list_numbers


def addition(list_numbers):  # do_something : change "Addition"
    result = sum(list_numbers)  # do_something : sum
    return result


def soustraction(list_numbers):
    i = 0
    for list_number in list_numbers:
        if i == 0:
            result = list_number
        else:
            result -= list_number
        i += 1
    return result


def multplication(list_numbers):
    for index, list_number in enumerate(list_numbers):
        if index == 0:  # do_something : remove ""
            result = list_number
        else:
            result *= list_number  # do_something : remove /
    return result


def division(list_numbers):
    for index, list_number in enumerate(list_numbers):
        if index == 0:
            result = list_number
        elif list_number == 0:
            print("Division par zéro impossible.")
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
    5. Quitter."""
    )
    while choice.isdigit():
        choice = int(choice)  # do_something : int()
        if choice < 5:
            if choice == 1:
                number = ask_user("Saisir un chiffre à ADDITIONNER ou clicker sur '=' ")
                list_numbers = values(number)
                result = addition(list_numbers)
            elif choice == 2:
                number = ask_user("Saisir un chiffre à SOUSTRAIRE ou clicker sur '=' ")
                list_numbers = values(number)
                result = soustraction(list_numbers)
            elif choice == 3:
                number = ask_user("Saisir un chiffre à MULTIPLIER ou clicker sur '=' ")
                list_numbers = values(number)
                result = multplication(list_numbers)
            elif choice == 4:
                number = ask_user("Saisir un chiffre à DIVISER ou clicker sur '=' ")
                list_numbers = values(number)
                result = division(list_numbers)
            message = f"Le resultat est ==> {result}"

        else:
            if choice == 5:
                message = "Goodbye"
        return print(message)
