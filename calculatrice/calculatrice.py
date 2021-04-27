def ask_user(func_name=None):
    if func_name:
        choice = input(f"""Saisir un chiffre à {func_name}\n>""")
    else:
        choice = input(
            """
    Tu veux :
    1. Additionner Tape 1
    2. Soustraire Tape 2
    3. Multiplier Tape 3
    4. Diviser Tape 4
    5. Quitter."""
        )
    return choice


def values(number, func_name):
    list_numbers = []
    while number.isdigit():
        list_numbers.append(int(number))
        number = ask_user(func_name)
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
        if index == 0:
            result = list_number
        else:
            result *= list_number
    return result


def division(list_numbers):
    for index, list_number in enumerate(list_numbers):
        if index == 0:
            result = list_number
        elif list_number == 0:
            print("Division par zéro impossible.")
            result = None
        else:
            result /= list_number
    return result


def display_interface():
    choice = ask_user()
    while choice.isdigit():
        choice = int(choice)  # do_something : int()
        if choice < 5:
            if choice == 1:
                func_name = "ADDITIONNER"
                number = ask_user(func_name)
                list_numbers = values(number, func_name)
                result = addition(list_numbers)
            elif choice == 2:
                func_name = "SOUSTRAIRE"
                number = ask_user(func_name)
                list_numbers = values(number, func_name)
                result = soustraction(list_numbers)
            elif choice == 3:
                func_name = "MULTIPLIER"
                number = ask_user(func_name)
                list_numbers = values(number, func_name)
                result = multplication(list_numbers)
            elif choice == 4:
                func_name = "DIVISER"
                number = ask_user(func_name)
                list_numbers = values(number, func_name)
                result = division(list_numbers)
            message = f"Le resultat est ==> {result}"

        else:
            if choice == 5:
                message = "Goodbye"
        return print(message)
