import random
from art.HigherLowerArt import logo, vs
from data.game_data import data
import os


def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take user's guess and follower counts and return if they got the right."""
    if a_followers > b_followers:
        if guess == "a":
            return True
        else:
            return False
    else:
        return guess == "b"


def play_higher_lower():
    print(logo)
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)

        if account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b)}.")
        guess = input("Who has more followers?Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        os.system('clear')
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score :{score}")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


play_higher_lower()
