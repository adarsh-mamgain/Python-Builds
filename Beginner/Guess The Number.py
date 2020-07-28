# import required modules
import random
from datetime import datetime

# these are iteration variables for loop and score
i = 0
point = 0
print("\n\n**************************************************")
print("|        Hi, this is simple guessing game        |")
print("|     You have three chance to play or guess     |")
print("|         Guess a number between 1 and 3         |")
print("**************************************************")

while i < 3:
	# seeding the random value as per the current time
	random.seed(datetime.now())

	# storing random values from 1 to 3, converting it
	# string to compare it with user input stored in 'answer' variable
	rand = str(random.randint(1,3))
	answer = input("\nYour Guess Number: ")
	print("The Random Number was: " + rand)

	# checking if the answer is right and assigning 1 point
	if(answer == rand):
		point += 1
		print("Wow! you guessed it right :)")

	# giving one more try/ chance
	elif(i < 2 and answer != rand):
		print("Oh no :( come on try again.")

	# finishing the while loop 
	else:
		print("\nGame Over")
	i+=1

# converting the point to string and storing it as 'score'
score = str(point)

# displaying the score if any
if(point > 0):
	print("\nYour score is: " + score)