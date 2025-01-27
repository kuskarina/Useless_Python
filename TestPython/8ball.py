import random as rd
import os

os.system('clear')
question = input("What is your question?   ")

number = rd.randint(0,4)

#print(number)

if number == 4:
	print("Try Again Later...")
if number == 3:
	print("Yes")
if number == 2:
	print("No")
if number == 1:
	print("I don't see that in your future...")
if number == 0:
	print("Sure, I guess")
