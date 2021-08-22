from random import random
import math
import random

minbet = 5
cardsindeck = 52
numofdeck = 0
numofplayers = input("Enter number of players:")

NumbersAlreadyPlayed = []


def randomnumber():
    num = math.floor(random.randint(0, 52))
 
    return num

print(randomnumber())


