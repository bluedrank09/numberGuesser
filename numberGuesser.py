# importing libraries
import sys
import random

# function for 
def getNumbers(userMax, userMin):
    userMin = int(input("Give me a minimum number for your range : "))
    userMax = int(input("Give me a maximum number for your range : "))
    return(userMin, userMax)

def guessing(randomNumber):
    userGuess = 0
    chancesLeft = userBet

    print(f"I am thinking of a number inside that range. Guess it !")
    userGuess = int(input('Whats your guess ? : '))

    if userGuess == randomNumber : 
        print(f"You did it, the answer was {userGuess}")

    while userGuess != randomNumber:
        if userGuess < randomNumber:
            print(f"Your guess of {userGuess} is too low. Try higher.")
            chancesLeft -= 1
            print(f"You have {chancesLeft} chances left ")
        elif userGuess > randomNumber:
            print(f"You guess of {userGuess} is too high. Try lower.")
            chancesLeft -= 1
            print(f"You have {chancesLeft} chances left ")
        
        userGuess = int(input('Whats your guess ? : '))

        if chancesLeft == 0:
            print(f"You have run out of moves. You have lost.")
        


if __name__ == "__main__":
    try:
        userBet = 0
        userMax = 0
        userMin = 0
        userBet = int(input("Whats your bet you're gonna wint his in three or less moves ? : "))
        print(f"{userBet}")
        userMin, userMax = (getNumbers(userMin, userMax))
        print(userMin)
        print(userMax)
        
        randomNumber = random.randrange(userMin, userMax, 1)
        print(randomNumber)

        guessing(randomNumber)


    except Exception as error:
        e_type, e_object, e_traceback = sys.exc_info()
        print(f"{e_type}, {e_object}")

    finally:
        print(f":)")