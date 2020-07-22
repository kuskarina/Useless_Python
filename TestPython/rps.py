from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to false
player = False

while player == False:
#set player to True
	player = input("Rock, Paper, Scissors?")
	if player == computer:
		print("Tie!")
	elif player == "Rock":
		if computer == "Paper":
			print("You loose!", computer, "covers", player)
		else:
			print("You win!", player, "smashes", computer)
	elif player == "Paper":
		if computer == "Scissors":
			print("You loose!", computer, "cuts", player)
		else:
			print("You win!", player, "covers", computer)
	elif player == "Scissors":
		if computer == "Rock":
			print("You loose...", computer, "smashes", player)
		else:
			print("You win!", player, "cuts", computer)
	else:
		print("That's not a valid play. Check your spelling!")
	player = False
	computer = t[randint(0,2)]
