import random
import sys
from enum import Enum

game_count = 0
def play_rps():
  class RPS(Enum):
      ROCK = 1
      PAPER = 2
      SCISSORS = 3
  
  print("\nWelcome to Rock-Paper-Scissors")

  # The users input options
  nonsos_choice = input("\nplease enter....\n\n1 for Rock,\n2 for Paper, or\n3 for Scissors\n\n")
  nonso = int(nonsos_choice)

  # Ensuring the user enters the right options
  if nonsos_choice not in ["1", "2", "3"]:
    print("you can only enter 1, 2, or 3")
    return play_rps()

  # computers choice
  computerschoice = random.choice([1, 2, 3])
  computer = int(computerschoice)

  # prints the result of the user and computer's choice
  print("\nyou chose" + " " + RPS(nonso).name + ".")
  print("\ncomputer chose" + " " + RPS(computer).name + ".")

  #Determines the winner
  def winner_decision(player, computer):
    if nonso == 1 and computer == 2:
      return  "yay!, nonso won🥇"
    elif nonso == 3 and computer == 2:
      return "congratulations nonso on your win!🎉"
    elif nonso == 1 and computer == 3:
      return "Nonso won again!🥳"
    elif nonso == computer:
      return "We have a tie!"
    else:
      return "🐍 computer wins!"
  game_choice = winner_decision(nonso, computer)  

 
  global game_count
  game_count += 1
  print("\nThe Game Count is: " + str(game_count))
  
  print("\n Play again?")
  while True:
    playagain = input("\n Y for yes \n\n Q for Quit!\n\n")  
    if playagain.lower() not in ["y", "q"]:
      continue
    else:
      break
  if playagain.lower() == "y":
      return play_rps()
  else:
    print("\n🥰🎉")
    print("thank you for playing!")
    sys.exit("Bye!, 👋")
play_rps()    