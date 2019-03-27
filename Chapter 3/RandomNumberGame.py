import random

secretNumber = random.randint(1,20)

print("Random Number Game!")
print("*******************")
print("Guess the number between 1 and 20: ")
guessedNumber = 0
guessed = False

def getNewGuess():
    global guessedNumber
    if guessedNumber != secretNumber:
        guessedNumber = int(input())
    while type(guessedNumber) != int or guessedNumber > 20 or guessedNumber < 1:
        print("Please enter a valid integer in the range 1-20: ")
        guessedNumber = int(input())

def makeGuess():
    global guessed
    while not guessed:
        getNewGuess()
        if guessedNumber == secretNumber:
            print("You win! You guessed the secret number!")
            guessed = True
        else:
            print("Incorrect, guess again!")
            if guessedNumber < secretNumber:
                print("[HINT] The secret number is larger than your guess.")
            else:
                print("[HINT] The secret number is smaller than your guess.")

makeGuess()
print("Exiting game...")