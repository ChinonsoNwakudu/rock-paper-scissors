# Rock-Paper-Scissors Game

## Description

This is a simple command-line implementation of the classic game Rock-Paper-Scissors written in Python. The game allows a user to play against- 
the computer. The computer randomly selects one of the three options: rock, paper, or scissors. The user inputs their choice, and the game decides the winner based on standard rules.

## Game Rules

The rules of the game are simple:

- **Rock** beats **Scissors** (Rock crushes Scissors)
- **Scissors** beats **Paper** (Scissors cut Paper)
- **Paper** beats **Rock** (Paper covers Rock)
- If both the player and the computer choose the same option, it results in a tie.

## Features

- User can choose between Rock, Paper, or Scissors.
- Computer makes a random choice between Rock, Paper, or Scissors.
- The game evaluates the winner based on the choices made.
- Displays the result of each round: win, lose, or tie.

## How to Run the Game

### Prerequisites

- Python 3.x should be installed on your computer. You can download it from [python.org](https://www.python.org/downloads/).

### Instructions

1. **Clone this repository to your local machine** using the following command:
    ```bash
    git clone https://github.com/your-username/rock-paper-scissors.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd rock-paper-scissors
    ```

3. **Run the Python script** to start the game:
    ```bash
    python rock_paper_scissors.py
    ```

4. **Follow the prompts**: Enter `1` for Rock, `2` for Paper, or `3` for Scissors when prompted.

## Game Logic

1. The game begins by asking the user to input their choice: `1` for Rock, `2` for Paper, or `3` for Scissors.
2. The user's input is validated to ensure it is one of the valid choices. If not, the program exits with a message indicating that only 1, 2, or 3 are acceptable inputs.
3. The computer makes a random choice from the same set of options (`1`, `2`, or `3`).
4. The user's choice and the computer's choice are then compared:
   - If both choices are the same, the game declares a tie.
   - If the user's choice beats the computer's choice (according to the rules above), the game declares the user as the winner.
   - Otherwise, the game declares the computer as the winner.
5. The results are displayed on the screen, indicating the choices made by both the user and the computer, and announcing the winner.

## Example Output

Welcome to Rock-Paper-Scissors!

Please enter: 1 for Rock, 2 for Paper, or 3 for Scissors

You chose Rock. Computer chose Scissors. Congratulations! You won! 🎉


## Future Improvements*

- Implement a scoring system to keep track of wins, losses, and ties over multiple rounds.
- Add a graphical user interface (GUI) to enhance user interaction.
- Provide an option to play best-of-three or best-of-five rounds.
- Include sound effects and animations for a more engaging experience.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute this software as per the terms of the license.

---

*Happy playing! 🎮*

