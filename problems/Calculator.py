import os

from problems.art.CalculatorArt import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Invalid number to divide on"


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}


def calculator():
    print(logo)

    first_number = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        calculation_function = operations[operation]
        result = calculation_function(first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ") == 'y':
            first_number = result
        else:
            should_continue = False
            os.system('clear')
            calculator()


calculator()