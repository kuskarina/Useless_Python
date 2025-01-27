from random import randint
import os

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to false
player = False
os.system('clear')


while player == False:
#set player to True
	player = input("Rock, Paper, Scissors? 'Exit' to quit!    ")
	if player == computer or player == str.lower(computer):
		print("Tie!")
	elif player == "Rock" or player == "rock":
		if computer == "Paper":
			print("You loose!", computer, "covers", player)
		else:
			print("You win!", player, "smashes", computer)
	elif player == "Paper" or player == "paper":
		if computer == "Scissors":
			print("You loose!", computer, "cuts", player)
		else:
			print("You win!", player, "covers", computer)
	elif player == "Scissors" or player == "scissors":
		if computer == "Rock":
			print("You loose...", computer, "smashes", player)
		else:
			print("You win!", player, "cuts", computer)
	elif player == "Exit" or player == "exit":
		print("Okay, thanks for playing!")
		quit()
		break
	else:
		print("That's not a valid play. Check your spelling!")
		computer = t[randint(0,2)]
	player = False
	computer = t[randint(0,2)]
