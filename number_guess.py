import random
import sys
def guess_number(name="newplayer"):
    game_count = 0
    newplayer_win = 0
    def play_guess_num():
        nonlocal name
        print(f"\n Hello {name}, Welcome to the Number-Guessing game!😀")
        
          # Input options for users
        newplayers_choice = input("\n Guess what number I am thinking of ...1, 2 or 3?\n\n")
        newplayer = int(newplayers_choice)
       # Ensuring the user enters the right options
        if newplayers_choice not in ["1", "2", "3"]:
            print("you can only choose 1, 2, or 3")
            return play_guess_num()

        Gamechoice_new = random.choice([1,2,3])
        Gamechoice = int(Gamechoice_new)

        # prints the result of the user and computer's choice
        print(f"{name} you chose {newplayer} ")
        print(f"I was thinking of the number {Gamechoice}")
        
        #determines the condition for winning and the number of times you win
        def winner_selection(player):
            nonlocal newplayer_win
            nonlocal name
            if newplayer == Gamechoice :
                print ("yay, you won🥇")
                newplayer_win +=1
            else:
                print ("sorry, better luck next timetime😢")
        choice = winner_selection(newplayer)        
        # Game counter; counts the number of times a person plays
        nonlocal game_count
        game_count +=1
        print(f"\nThe Game Count is: {game_count}")
        print(f"{name}'s win: {newplayer_win}")

        print(f"\n Play again, {name}?")
        while True:
            playagain = input("\n Y for yes \n\n Q for Quit!\n\n")  
            if playagain.lower() not in ["y", "q"]:
             continue
            else:
             break
        if playagain.lower() == "y":
           return play_guess_num()
        else:
            print("\n🥰🎉")
            print("thank you for playing!")
            sys.exit(f"Bye {name}!, 👋")        
    play_guess_num()
if __name__ == "__main__":
  import argparse


  parser = argparse.ArgumentParser(
        description="provides a personalized Gaming experience for the Number-Guess game"
    )

  parser.add_argument("-n", "--name", metavar="name",required=True, help= "input the name of the person playing")
  args = parser.parse_args()
    
number_guess = guess_number(args.name)
number_guess()