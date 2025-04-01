import random
import time

def difficulty():
    while True:
        select_difficulty = str.casefold(input("Choose your difficulty (easy/hard): "))
        if select_difficulty == "easy":
            easy_mode()
            break
        elif select_difficulty == "hard":
            hard_mode()
            break
        else:
            print("Invalid choice, please try again.")

def player_choose():
    playerchoice = str.casefold(input("Choose your weapon (Rock/Paper/Scissors): "))
    if playerchoice not in ["rock", "paper", "scissors", "gun"]:
        print("Invalid choice, please try again.")
        return player_choose()
    return playerchoice

def computer_choose():
    computerchoice = random.choice(["rock", "paper", "scissors"])
    return computerchoice

def determine_winner(playerchoice, computerchoice):
    print(f"I choose {computerchoice}")
    print(f"You have chosen {playerchoice}")
    if playerchoice == computerchoice:
        print("It's a tie!")
        return "tie"
    elif (playerchoice == "rock" and computerchoice == "scissors") or \
         (playerchoice == "paper" and computerchoice == "rock") or \
         (playerchoice == "scissors" and computerchoice == "paper"):
        print("You win!")
        return "win"
    elif playerchoice == "gun":
        print("Wait a minute, that's illegal!")
        return "illegal"
    else:
        print("You lose!")
        return "lose"

def easy_mode():
    playerchoice = player_choose()
    computerchoice = computer_choose()
    determine_winner(playerchoice, computerchoice)

def hard_mode_logic(playerchoice):
    if playerchoice == "rock":
        return "paper"
    elif playerchoice == "paper":
        return "scissors"
    elif playerchoice == "scissors":
        return "rock"

def special_sequence():
    print("Good thing I have my kevlar vest on!")
    print("You lose!")

def hard_mode():
    playerchoice = player_choose()
    if playerchoice == "gun":
        return special_sequence()
    else:
        computerchoice = hard_mode_logic(playerchoice)
        determine_winner(playerchoice, computerchoice)

def end_game():
    print("Thanks for playing!")
    time.sleep(0.5)
    restart = str.casefold(input('Press "enter" to play again or type "exit" to quit: '))
    if restart == "":
        return True
    else:
        return False


def game():
    difficulty()
    return end_game()

while game():
    pass