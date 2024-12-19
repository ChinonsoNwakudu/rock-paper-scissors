import random
import sys
from enum import Enum

def RPS(name="PlayerOne"):
   game_count = 0
   PlayerOne_wins = 0
   computer_wins = 0
   def play_rps():
      nonlocal name
      nonlocal PlayerOne_wins
      nonlocal computer_wins
      class RPS(Enum):
          ROCK = 1
          PAPER = 2
          SCISSORS = 3
      
      print("\nWelcome to Rock-Paper-Scissors")

      # The users input options
      PlayerOnes_choice = input(f"\n{name}, please enter....\n\n1 for Rock,\n2 for Paper, or\n3 for Scissors\n\n")
      PlayerOne = int(PlayerOnes_choice)

      # Ensuring the user enters the right options
      if PlayerOnes_choice not in ["1", "2", "3"]:
        print(f"{name}, you can only enter 1, 2, or 3")
        return play_rps()

      # computers choice
      computerschoice = random.choice([1, 2, 3])
      computer = int(computerschoice)

      # prints the result of the user and computer's choice
      print(f"\n{name} chose  {RPS(PlayerOne).name }.")
      print(f"\ncomputer chose  {RPS(computer).name} .")

      #Determines the winner
      def winner_decision(player, computer):
        nonlocal name
        nonlocal PlayerOne_wins
        nonlocal computer_wins
        if PlayerOne == 1 and computer == 2:
          PlayerOne_wins +=1
          return  "yay!, {name} won🥇"
        elif PlayerOne == 3 and computer == 2:
          PlayerOne_wins +=1
          return  "yay!, {name} won🥇"
        elif PlayerOne == 1 and computer == 3:
          PlayerOne_wins +=1
          return  "yay!, {name} won🥇"
        elif PlayerOne == computer:
          return "We have a tie!"
        else:
          computer_wins +=1
          return f"🐍 computer wins! \nSorry {name}.."
      game_choice = winner_decision(PlayerOne, computer)  

    # counts the number of times a person plays
      nonlocal game_count
      game_count += 1

      print(f"\nThe Game Count is:  {game_count}")
      print(f"\n{name}'s wins:  {PlayerOne_wins}")
      print(f"\nComputer wins:  {computer_wins}")
      
      # option to play again, choose 'y' for yes and 'q' to quit
      print(f"\n Play again, {name}?")
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
        sys.exit(f"Bye {name}!, 👋")
   return play_rps      
 
if __name__ == "__main__":
  import argparse


  parser = argparse.ArgumentParser(
        description="provides a personalized Gaming experience"
    )

  parser.add_argument("-n", "--name", metavar="name",required=True, help= "input the name of the person playing")
  args = parser.parse_args()

  rock_paper_scissors = RPS(args.name)   
  rock_paper_scissors()