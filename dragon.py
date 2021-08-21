import random
import time


def displayIntro():
    print(
        """You are in a land full of dragons. In front of you,
           you see two caves. In one cave, the dragon is friendly
           and will share his treasure with you. The other dragon
           is greedy and hungry, and will eat you on sight."""
    )
    print()


def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you go into? (1 or 2)")
        cave = input()

    return cave


def sell_or_go():
    """Spend money or go home"""
    print('Would you like to sell your treasure or go home? (s or g)')
    to_sell_or_go = input()
    if  to_sell_or_go.lower() == 's':
        print('You sell all your treasure and become a zillionare')
    if to_sell_or_go.lower() == 'g':
        print('You go home, remembering the grand adventure you had.')


def checkCave(chosenCave):
    print("You approach the cave...")
    time.sleep(2)
    print("it is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("Gives you his treasure")
        sell_or_go()
    else:
        print("Gobbles you down in one bite!")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Do you want to play again? (yes or no)")
    playAgain = input()
