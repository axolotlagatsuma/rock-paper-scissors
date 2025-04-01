from numpy import random
import time

def playerchoose():
    global p_wp
    p_wp = input("Choose your weapon (Rock/Paper/Scissors): ")
    if str.casefold(p_wp) == str("rock"):
        p_wp = 1
    elif str.casefold(p_wp) == str("paper"):
        p_wp = 2
    elif str.casefold(p_wp) == str("scissors"):
        p_wp = 3
    elif str.casefold(p_wp) == str("gun"):
        p_wp = 4
    else:
        playerchoose()

def rock():
    if p_wp == 1:
        print("It's a tie!")
    elif p_wp == 2:
        print("You win!")
    elif p_wp == 3:
        print("You lose!")


def paper():
    if p_wp == 1:
        print("You lose!")
    elif p_wp == 2:
        print("It's a tie!")
    elif p_wp == 3:
        print("You win!")


def scissors():
    if p_wp == 1:
        print("You win!")
    elif p_wp == 2:
        print("You lose!")
    elif p_wp == 3:
        print("It's a tie!")

def compchoose():
    c_wp = random.randint(1,3)
    if c_wp == 1:
        print("I choose rock")
        rock()
    elif c_wp == 2:
        print("I choose paper")
        paper()
    else:
        print("I choose scissors")
        scissors()

def hardmode():
    if p_wp == 1:
        print("I choose paper")
        print("You lose!")
    elif p_wp == 2:
        print("I choose scissors")
        print("You lose!")
    elif p_wp == 3:
        print("I choose rock")
        print("You lose!")
    elif p_wp == 4:
        print("Good thing I got my kevlar vest today.")
        print("You lose!")

def diff():
    global difficulty
    difficulty = input("Enter the difficulty level (Easy/Hard): ")

def end():
    print("\nThanks for playing!")
    time.sleep(1)
    restart = input("Press Enter to restart or type 'exit' to quit: ")
    if str.casefold(restart) == "exit" :
        exit()
    elif restart == "":
        diff()
        game()
    else:
        exit()

def game():
    if str.casefold(difficulty) == str("easy"):
        playerchoose()
        if p_wp == 4:
            print("Woah, woah calm down okay you win!")
            end()
        else:
            compchoose()
            end()
    elif str.casefold(difficulty) == str("hard"):
        playerchoose()
        hardmode()
        end()
    else:
        diff()

diff()
game()