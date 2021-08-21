"""Guess the Number game"""

import random

GUESSES_TAKEN = 0


print("Hello, what is your name?")
myName = input()


NUMBER = random.randint(1, 20)

print(f"Well {myName} I am thinking of a number between 1 and 20.")

for GUESSES_TAKEN in range(6):
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    if guess < NUMBER:
        print("Your guess is too low.")

    if guess > NUMBER:
        print("Your guess is too high.")

    if guess == NUMBER:
        break

if guess == NUMBER:
    GUESSES_TAKEN = str(GUESSES_TAKEN + 1)
    print(f"Good job, {myName}! You guessed the number in {GUESSES_TAKEN} guesses!")
if guess != NUMBER:
    NUMBER = str(NUMBER)
    print(f"Nope.  The number I was thinking of was {NUMBER}.")
