import random

HANGMAN_PICS = [
    """
    +---+
        |
        |
        |
        ===""",
    """
    +---+
    O   |
        |
        |
        ===""",
    """
    +---+
    O   |
    |   |
        |
        ===""",
    """
    +---+
    O   |
    /|   |
        |
        ===""",
    """
    +---+
    O   |
    /|\  |
     |
        ===""",
    """
    +---+
    O   |
    /|\  |
    /    |
        ===""",
    """
    +---+
    O   |
    /|\  |
    / \  |
        ===""",
    """
   +---+
   O   |
  /|\  |
  / \  |
      ===""",
    """
   +---+
  [O]  |
  /|\  |
  / \  |
      ===""",
]


words = {
    "Colors": "red orange yellow green blue indigo violet white black brown".split(),
    "Shapes": "square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon".split(),
    "Fruits": "apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato".split(),
    "Animals": "bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra".split(),
}


def getRandomWord(wordDict):
    """This function returns a random string from the passed list of strings"""
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]


def displayBoard(missedLetters, correctLetters, secretWord):

    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Missed letters:", end=" ")
    for letter in missedLetters:
        print(letter, end=" ")
    print()

    blanks = "_" * len(secretWord)

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1 :]

    for letter in blanks:  # show the secret word with spaces inbetween each letter
        print(letter, end=" ")
    print()


def get_Guess(alreadyGuessed):
    # returns the letter the player entered.  This function makes sure the player entered a single letter and not something else
    while True:
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter.  Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a LETTER")
        else:
            return guess


def playAgain():
    # This function returns true if the player wants to play again; otherwise it returns false
    print("Do you want to play again(yes or no)")
    return input().lower().startswith("y")


print("H A N G M A N")
difficulty = 'X'
while difficulty not in 'EMH':
    print('Enter difficultly: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()

if difficulty == "M":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]


if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ""
correctLetters = ""
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter
    guess = get_Guess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f"Yes! The secret word is {secretWord}!  You have won!")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # check if player has guess too many times and lost
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            number_of_tries = str(len(missedLetters))
            number_of_correct_guesses = str(len(correctLetters))
            print(
                f"You have run out of guesses! After {number_of_tries} missed guesses and {number_of_correct_guesses} correct guesses. \n"
            )
            print(f"The word was {secretWord}")
            gameIsDone = True

        # Ask the player if they want to play again (but only if the game is done)
    if gameIsDone:
        if playAgain():
            missedLetters = ""
            correctLetters = ""
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
