from random import random
import math
import random

minbet = 5
cardsindeck = 52
numofdeck = 0
numofplayers = input("Enter number of players: ")

NumbersAlreadyPlayed = []



def randomnumber():
    num = math.floor(random.randint(0, 52))
    NumbersAlreadyPlayed.append(num)
    return num
    #continue
    #break

#def define(newlist):
#    for num in newlist:
#        if num == randomnumber():
#            return num
    #break
