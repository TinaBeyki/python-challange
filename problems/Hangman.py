import random
# import HangmanArt
from HangmanArt import stages

print("Hint: its yummy summer fruit ")
word_list = ["kiwi", "strawberry", "blueberry"]
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6

# create blanks
display = []
for letter in chosen_word:
    display += "_"

end_of_game = False

while not end_of_game:
    guss = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        # check guessed letter
        if guss == letter:
            display[i] = letter
    print(display)

    if guss not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            # print(HangmanArt.stages[0]) -> import Hangman
            print(stages[0])
            print("You Lose :(")
            break

    if "_" not in display:
        end_of_game = True
        print("You Won yo ho :)")
        break

    print(stages[lives])
