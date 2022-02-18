''' Write a python prog capable of playing this game(Snake, Water, Gun) with the user.'''

import random

rand = random.randint(1,3)

if rand==1:
    compturn = "Snake"
elif rand==2:
    compturn = "Water"
elif rand==3:
    compturn = "Gun"

player = input("Your Turn(Enter Snake or Water or Gun)")

def Game(compturn, player):
    if compturn==player:
        print("Its a Tie!!")
    elif compturn=="Snake":
        if player=="Gun":
            print("You won!!!")
        elif player=="Water":
            print("You Lost!!!")

    elif compturn=="Water":
        if player=="Snake":
            print("You won!!!")
        elif player=="Gun":
            print("You Lost!!!")
    
    elif compturn=="Gun":
        if player=="Snake":
            print("You Lost!!!")
        elif player=="Water":
            print("You won!!!")

print("Computer chose ", compturn)
print("You chose ", player)
Game(compturn, player)


