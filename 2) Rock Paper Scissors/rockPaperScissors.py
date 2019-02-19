import random # Import the random module
'''
To call functions from the 'random' module, I need to call 'random' first.
Ex: random.randInt()

If I didn't want to call 'random' so I could just say randInt(), I'd write:
from random import *
'''

print("Games by Tim presents...")
print("---------------------")
print("ROCK, PAPER, SCISSORS\n      Best to 3")
print("---------------------")

yourScore = 0
cpuScore = 0
validMoves = ("R", "P", "S") # tuple
dict = {"R": "rock", "P": "paper", "S": "scissors"} # dictionary

def didYouWin(you, cpu): # Return 0 for lose, 1 for tie, 2 for win
    global yourScore
    global cpuScore
    if you == cpu:
        return 1
    elif you == "R" and cpu == "S" or you == "P" and cpu == "R" or you == "S" \
    and cpu == "P":
        yourScore += 1
        return 2
    else:
        cpuScore += 1
        return 0

def rpsGame():
    yourMove = input("\nR for rock, P for paper, or S for scissors: ").upper()
    while yourMove not in validMoves:
        yourMove = input("That's not an R, P, or S. Try again: ").upper()
    cpuMove = validMoves[random.randint(0,2)] # Pseudorandom number from 0-2
    print("\nYou chose " + dict[yourMove] + ". I chose " + dict[cpuMove] + ".")
    result = didYouWin(yourMove, cpuMove)
    if result == 0:
        print("You lose this round.")
    elif result == 1:
        print("We tied this round.")
    else:
        print("You win this round.")
    print("Score: " + str(yourScore) + "-" + str(cpuScore))

while yourScore < 3 and cpuScore < 3:
    rpsGame()

if yourScore >= 3:
    print("\nOh hey, you won the game.")
if cpuScore >= 3:
    print("\nAww man, you lost the game.")
