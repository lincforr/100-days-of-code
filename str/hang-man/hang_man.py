# Hang Man
# https://app.diagrams.net/#Hlincforr%2F100-days-of-code%2Fmain%2Fstr%2Fhang-man%2Fhangman.drawio
import random

# get word
word_list = ["ardvark", "baboon", "camel", "apple"]
chosen_word = random.choice(word_list)

# get _ for each letter
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

# testing code
print(f'Pssst, the solution is {chosen_word}.')

# guessing code
guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    # testing code
    # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
        display[position] = letter

print(display)