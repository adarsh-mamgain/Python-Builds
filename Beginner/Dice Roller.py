# import required modules
import random
from datetime import datetime

print("\n\n*************************************")
print("|     |     |     |     |     |     |")
print("|  1  |  2  |  3  |  4  |  5  |  6  |")
print("|     |     |     |     |     |     |")
print("*************************************")

print("\n<--------Generate random numbers through this dice-------->")
print("Enter 'y' to rotate, 'n', 'quit' or 'exit' to leave the game\n")

# the iteration variable for loop
cond = True

while cond:
	# seeding the random value as per the current time
	random.seed(datetime.now())
	answer = input("Rotate: ")

	# execute as per user inputs
	if(answer == "y"):
		# storing random values from 1 to 6, converting it
		# to string to print it during concatenation
		rand = str(random.randint(1,6))
		print("The number is: ")
		print("|‾‾‾‾‾|")
		print("|  " + rand + "  |")
		print("|_____|\n")

	# finishing the while loop, when user wants to exit
	elif(answer == "n" or answer == "exit" or answer == "quit"):
		cond = False

	# printing if user inputs anything else
	else:
		print("\nChoose a correct option!!")

# displaying that you are out of the dice game
print("\nYou are out of the game")