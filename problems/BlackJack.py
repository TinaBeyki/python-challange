"""
BlackJack or 21
"""
import os
import random

from art.BlackJackArt import logo


def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # last 3 tens are value of Jack, Queen, King
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # ace can be both 1 and 11
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_final_score, computer_final_score):
    """Takes both user score and computer score and compare them to show who is the winner."""
    if user_final_score == computer_final_score:
        return "Draw"
    elif computer_final_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_final_score == 0:
        return "Win with Blackjack"
    elif user_final_score > 21:
        return "You went over. You lose"
    elif computer_final_score > 21:
        return "Opponent went over. You win"
    elif user_final_score > computer_final_score:
        return "You win"
    else:
        return "You lose"


def play_blackjack():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    """ 
    we cant use user_cards += new_card unless new_card was a list
    new_card = [deal_card]
    user_cards += new_card or user_cards.extend(new_card) was ok, but now error occurs because new_card is not iterable
    """
    for _ in range(2):
        # new_card = deal_card()
        # user_cards.append(new_card)
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}\n")
        print(f"    Computer's first card: {computer_cards[0]}\n")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

        """
        Once the user is done, it's time to let the computer play. 
        The computer should keep drawing cards as long as it has a score less than 17
        """
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    os.system('clear')
    play_blackjack()

