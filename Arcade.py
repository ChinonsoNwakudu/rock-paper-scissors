from number_guess import number_guess
from RPS import RPS
import sys

def arcade_game(name="mainplayer"):
   

    print(f"\n{name}, Welcome to the Arcade, select your game and have fun!\n\n")

    game_choice = input("\n Please your game of choice:\n 1 = Rock Paper Scissors\n 2 = Guess My Number\n\n or press \"x\" to exit\n\n" )
    
    if game_choice == 1:
       num_guess = number_guess(name)
       num_guess()
  
    elif game_choice == 2:
        rock_paper_scissors = RPS(args.name)   
        rock_paper_scissors()
    elif game_choice == "x":
        print("Thank you for playing" )
        sys.exit(f"Bye {name}!, 👋")
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(   description="provides a personalized Gaming experience" )

    parser.add_argument("-n", "--name", metavar="name",required=True, help= "input the name of the person playing")
    args = parser.parse_args()
    
    arcade_game(args.name)
   
