from random import randrange
from art import logo

print(logo)

def pick_number():
    number = randrange(1, 100)
    return number

PICKED_NUMBER = pick_number()

attempts = 0

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")
dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if dificulty == "easy":
    attempts += 10
else:
    attempts += 5
print(f"You have {attempts} left in the game")


while attempts > 0:
    guessed_number = int(input("Make a guess: "))
    if guessed_number > PICKED_NUMBER:
        print("Too high")
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    elif guessed_number < PICKED_NUMBER:
        print("Too low")
        attempts -= 1
        print(f"You have {attempts} attempts left.")
    elif guessed_number == PICKED_NUMBER:
        print(f"You Win! The number was {PICKED_NUMBER}")
        exit()

print(f"You loose the number was {PICKED_NUMBER}.")
exit()