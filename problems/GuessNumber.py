import random
from art.GuessNumberArt import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def compare_to_answer(result, your_guess, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if result > your_guess:
        print("Too low.")
        return turns - 1
    elif result < your_guess:
        print("Too hight.")
        return turns - 1
    else:
        print(f"You got it! The answer was {result}")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    elif difficulty == 'hard':
        return HARD_LEVEL_TURNS


def play_guess_number():
    print(logo)

    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.\n")
    answer = random.randint(1, 100)

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = compare_to_answer(answer, guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


play_guess_number()