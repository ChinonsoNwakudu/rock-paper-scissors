import random
import sys
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER =2
    SCISSORS = 3

print("")
nonsoschoice = input("please enter....\n\n1 for Rock,\n2 for Paper, or\n3 for Scissors\n\n")

nonso = int(nonsoschoice)

if nonso < 1 or nonso >3:
   sys.exit("you can only enter 1, 2, or 3")

computerschoice = random.choice('123')
computer = int(computerschoice)

print("you chose" + " " + str((RPS(nonso))).replace('RPS.', "  ") + ".")
print("computer chose" + " " + str((RPS(computer))).replace('RPS.', " ") + ".")

if "nonso = 1 and computer = 2":
  print("yay!, nonso won🥇")
elif "nonso = 3 and computer = 2":
   print("congratulations nonso on your win!🎉") 
elif "nonso = 1 and computer = 3":
  print("Nonso won again!🥳")
elif "nonso = computer":
  print("We have a tie!")
else:
  print("🐍 computer wins!")
