import random
def getValidNum(prompt):
    while True:
        try:
            userNum = int(input(prompt))
            return userNum
        except ValueError:
            print("Oops! You need to enter an integer. Enter in an integer.")
def number_guessing_game():
    # Print out a cool multi-line message to welcome them to the game
    # Program picks a random number
    # User is asked to guess the number
    # Game continues until they guess it right (program tells them to guess higher or lower each time)
    # add in some error handling so if they put in a non-integer it tells them to try again, but doesn't end the program.
    print("Welcome to the number guessing game!")
    print("Try to guess it, I will tell you if it is too low or high")
    randomNum = random.randint(0,100)
    while True:
        userNum = getValidNum("Enter a number:")
        if userNum > randomNum:
            print("Guess is too high. Try a lower number")
        elif userNum < randomNum:
            print("Guess is too low. Try a higher number.")
        else:
            print(f"You guessed the right number! It was {randomNum}.")
            break
    print("Thanks for playing!")
    print()
    number_guessing_game()
if __name__ == "__main__":
    number_guessing_game()