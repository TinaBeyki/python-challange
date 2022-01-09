import time

from data.coffee_machine_data import resources, menu
import os
from art.CoffeeMachineArt import logo, out_of_service

is_on = True
requirements_available = True
profit = 0


def is_resource_sufficient(order_ingredients):
    """Takes the flavor and checks if the resource is sufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True


def process_coins():
    """Takes coins and returns total amount"""
    print("Please insert coins: ")
    input_counts = [int(input("How many quarters? ")) * 0.25, int(input("How many dimes? ")) * 0.10,
                    int(input("How many nickels? ")) * 0.05, int(input("How many pennies? ")) * 0.01]
    counts_sum = sum(input_counts)
    return counts_sum


def is_transaction_sufficient(money_recieved, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_recieved == drink_cost:
        global profit
        profit += drink_cost
        return True
    elif money_recieved > drink_cost:
        print(f"Please take the rest of your money from the machine:)")
        return True
    else:
        print(f"Sorry that's not enough money, Money refunded.")
        return False


def coffee_machine():
    global is_on, requirements_available

    while is_on:
        print(logo)
        print("-------------------------------------------------------------------------------------------------------")
        choice = input("What would you like? (espresso/latte/cappuccino): ")

        # handle user choice -------------------------------
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water: {resources['water']}")
            print(f"Coffee: {resources['coffee']}")
            print(f"Milk: {resources['milk']}")
        else:
            drink = menu[choice]  # drink is espresso or latte or cappuccino
            if is_resource_sufficient(drink["ingredients"]):
                print(f"You need to pay ${drink['cost']}")
                payment = process_coins()  # payment is the total amount of coins
                is_sufficient = is_transaction_sufficient(payment, drink["cost"])
                if is_sufficient:
                    for item in resources:
                        resources[item] -= drink["ingredients"][item]  # updating the resources
                    print(f"Here is your {drink} enjoy it:)")
                time.sleep(10)
                os.system('clear')
    print(out_of_service)


coffee_machine()
