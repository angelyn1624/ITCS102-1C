import random

print("number guessing game")
print("++++++++++++++++++++++++++++++")

random_value = random.randint(1,100)
tries = 0 
tuloy = True 

name = input("input your name -->")

while tuloy == True:
	num = eval(input("guess a number from 1 to 100 --> "))

	if num == random_value:
		tries +=1
		print("winner !!!")
		print(f"hi {name}, your guess is correct, number of tries")