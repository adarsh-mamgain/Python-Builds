import random
from datetime import datetime

i = 0
point = 0
print("\n\n******** Hi, this is simple guessing game ********")

while i < 3:
	random.seed(datetime.now())
	rand = str(random.randint(1,3))
	answer = input("\nGuess a number between 1 and 5:\n")
	print(rand)
	if(answer == rand):
		point += 1
		print("Wow! you guessed it right :)")
	elif(i < 2):
		print("Oh no :( come on try again.")
	else:
		print("\nGame Over")
	i+=1
score = str(point)
if(point > 0):
	print("Your score is: " + score)