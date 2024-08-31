import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER =2
    SCISSORS = 3

print("\nWelcome to Rock-Paper-Scissors")

# The users input options
nonsos_choice = input("please enter....\n\n1 for Rock,\n2 for Paper, or\n3 for Scissors\n\n")
nonso = int(nonsos_choice)

# Ensuring the user enters the right options
if nonso < 1 or nonso >3:
   sys.exit("you can only enter 1, 2, or 3")

# computers choice
computerschoice = random.choice([1, 2, 3])
computer = int(computerschoice)

# prints the result of the user and computer's choice
print("you chose" + " " + RPS(nonso).name + ".")
print("computer chose" + " " + RPS(computer).name + ".")

#Determines the winner
if nonso == 1 and computer == 2:
  print("yay!, nonso won🥇")
elif nonso == 3 and computer == 2:
   print("congratulations nonso on your win!🎉") 
elif nonso == 1 and computer == 3:
  print("Nonso won again!🥳")
elif nonso == computer:
  print("We have a tie!")
else:
  print("🐍 computer wins!")