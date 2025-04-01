import random
import time

def difficulty():
    difficulty = str.casefold(input("Choose your difficulty (easy/hard): "))
    if difficulty == "easy":
        easyMode()
    elif difficulty == "hard":
        hardMode()
    else:
        print("Invalid choice, please try again.")
        return difficulty()

def playerChoose():
    playerchoice = str.casefold(input("Choose your weapon (Rock/Paper/Scissors): "))
    if playerchoice not in ["rock", "paper", "scissors", "gun"]:
        print("Invalid choice, please try again.")
        return playerChoose()
    return playerchoice

def computerChoose():
    computerchoice = random.choice(["rock", "paper", "scissors"])
    return computerchoice

def determineWinner(playerchoice, computerchoice):
    print("I choose " + str(computerchoice))
    print("You have chosen " + str(playerchoice))
    if playerchoice == computerchoice:
        print("It's a tie!")
    elif playerchoice == "rock" and computerchoice == "scissors" or playerchoice == "paper" and computerchoice == "rock" or playerchoice == "scissors" and computerchoice == "paper":
        print("You win!")
    elif playerchoice == "gun":
        print("Wait a minute, that's illegal!")
    else:
        print("You lose!")

def easyMode():
    playerchoice = playerChoose()
    computerchoice = computerChoose()
    determineWinner(playerchoice, computerchoice)

def hardModeLogic(playerchoice):
    if playerchoice == "rock":
        return "paper"
    elif playerchoice == "paper":
        return "scissors"
    elif playerchoice == "scissors":
        return "rock"

def specialSequence():
    print("Good thing I have my kevlar vest on!")
    print("You lose!")

def hardMode():
    playerchoice = playerChoose()
    if playerchoice == "gun":
        return specialSequence()
    else:
        computerchoice = hardModeLogic(playerchoice)
        determineWinner(playerchoice, computerchoice)

def endGame():
    print("Thanks for playing!")
    time.sleep(0.5)
    restart = str.casefold(input('Press "enter" to play again or type "exit" to quit: '))
    if restart == "":
        game()
    else:
        exit()


def game():
    difficulty()
    endGame()

game()
