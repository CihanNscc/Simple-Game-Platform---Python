# 🎮 Simple Game Platform - Python

This is a Python-based game platform where you can play three different games:

- Rock Paper Scissors
- Number Guessing Game
- Dice Rolling Game

This is a simple showcase of common programming concepts in Python.

## 🚀 Concepts

### Object-Oriented Programming (OOP):

- **Classes and Objects:** The project uses classes to define different types of games, such as RockPaperScissorsGame, NumberGuessingGame, and DiceRollingGame, which all inherit from a base Game class.
- **Inheritance:** The Game class provides shared functionality, and each specific game class (e.g., RockPaperScissorsGame) inherits from it and adds game-specific logic.
- **Encapsulation:** Certain methods and attributes are made private (e.g., using \_\_method_name) to hide internal logic from outside interference, promoting better design.

### User Input Handling:

- The project makes extensive use of user input through the input() function, and employs loops and conditions to validate and respond to user choices, such as choosing a game or making decisions within a game.
- It demonstrates best practices for handling invalid input and prompting users until they enter correct information.

### Control Flow:

- The project uses conditional statements (if, elif, else) to compare the player's choices against the computer's choices and determine outcomes.
- Loops: while loops are used to continuously run game rounds and request input until a valid response or a specific condition (e.g., quitting the game) is met.

### Function Abstraction:

- Common functionality, such as asking for a yes/no input, is abstracted into reusable functions like get_yes_no_input() to reduce code duplication and increase clarity.

### Error Handling:

- The program handles common errors, such as invalid inputs, by using loops and conditional checks to ensure the user provides appropriate input before proceeding.

### Modularization:

- The project is divided into logical sections, with each class and function serving a distinct purpose. This modularity makes the code more maintainable and scalable.

### Input and Output:

- The project emphasizes how to interact with users through the terminal, displaying messages and receiving input in a user-friendly manner.

## 📜 How to Run

### Prerequisites:

- Python 3.x installed on your system.

### Steps to Run:

1. Clone this repository or download the Python file.
2. Open your terminal or command prompt.
3. Navigate to the folder where the file is located.
4. Run the following command:

```bash
python game_platform.py
```

Follow the prompts to select a game and start playing.

## 🎲 Available Games

1. **Rock Paper Scissors**

   - Choose between Rock, Paper, or Scissors.
   - Play against the computer and see if you can beat its choice!

2. **Number Guessing Game**

   - The computer will select a random number between 1 and 100.
   - You have 5 chances to guess the correct number. Hints will be provided after each guess.

3. **Dice Rolling Game**
   - Both you and the computer will roll a virtual die.
   - The one with the higher number wins, or it’s a draw if the numbers are equal.

## 💻 Code Overview

### Main Components:

- **Game class**: A base class containing shared functionality such as game stats and the game loop.
- **RockPaperScissorsGame class**: Handles the logic for Rock Paper Scissors, including user input and determining the winner.
- **NumberGuessingGame class**: Manages the number guessing game logic and checks guesses against a randomly generated number.
- **DiceRollingGame class**: Simulates rolling dice for both the player and the computer to determine the winner.

### Game Flow:

- Users are greeted and prompted to select a game.
- After each round, users can choose to play again or switch games.
- Statistics are displayed at the end of each game session.

## 📂 File Structure

├── game_platform.py # Main Python file containing all the game logic
└── README.md # This README file
└── LICENSE # License information

## 🛠️ Customization

You can easily modify the following constants in the `game_platform.py` file to adjust game settings:

- **NUMBER_OF_GUESSES**: Number of attempts allowed in the Number Guessing Game (default is 5).
- **LOWEST_NUMBER** and **HIGHEST_NUMBER**: The range of numbers for the Number Guessing Game.
- **HIGHEST_DICE_VALUE**: The maximum value on the dice for the Dice Rolling Game (default is 6).

## 📝 License

This project is open source and available under the MIT License.
