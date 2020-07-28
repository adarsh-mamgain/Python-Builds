# importing random module
import random

# loop condition
cond = True

# intro output for users
print("|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
print("|     Welcome to Rock, Paper & Scissors     |")
print("|     Type 'rock', 'paper' or 'scissors'    |")
print("|-------------------------------------------|")
print("|              as your answer               |")
print("|  Type 'quit' or 'exit' to stop the game   |")
print("|___________________________________________|\n")

while cond:
    # choice list
    choiceList = ["rock", "paper", "scissors"]
    # choose randomly from the list
    guess = random.choice(choiceList)
    # players scoring
    score = 0
    computer = 0

    # asking input for the guess
    answer = input("\nYou choose: ")

    if(answer != "quit" or answer != "exit"):
        print("Computer choose: " + guess)

    # conditions for user's input and further,
    # conditions for comparing it with computer's guess
    if(answer == "quit" or answer == "exit"):
        cond = False
    elif(answer == guess):
        print("It's a draw!")
    elif(answer == "rock"):
        if(guess == "paper"):
            computer += 1
            compPoint = str(computer)
            print("COMPUTER: " + compPoint + " point")
        else:
            score += 1
            playerScore = str(score)
            print("PLAYER: " + playerScore + " point")
    elif(answer == "paper"):
        if(guess == "scissors"):
            computer += 1
            compPoint = str(computer)
            print("COMPUTER: " + compPoint + " point")
        else:
            score += 1
            playerScore = str(score)
            print("PLAYER: " + playerScore + " point")
    elif(answer == "scissors"):
        if(guess == "rock"):
            computer += 1
            compPoint = str(computer)
            print("COMPUTER: " + compPoint + " point")
        else:
            score += 1
            playerScore = str(score)
            print("PLAYER: " + playerScore + " point")
    else:
        print("Please input correct option!")