# Hang Man
# https://app.diagrams.net/#Hlincforr%2F100-days-of-code%2Fmain%2Fstr%2Fhang-man%2Fhangman.drawio
import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
