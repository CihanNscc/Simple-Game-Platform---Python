import random

# List of games available on the platform
list_of_games = [
    "Rock Paper Scissors",
    "Number Guessing Game",
    "Dice Rolling Game",
]

# Constants for the games
NUMBER_OF_GUESSES = 5
LOWEST_GUESS_NUMBER = 1
HIGHEST_GUESS_NUMBER = 100
HIGHEST_DICE_VALUE = 6


# Function to get yes or no input from the player
def get_yes_no_input(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ["y", "n"]:
            return choice == "y"
        print("Invalid input. Please enter 'y' or 'n'.")


# Base class for all games
class Game:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0

    # Greeting method to welcome players to the game
    def greet(self):
        print(f"Welcome to {self.name.lower()} game.")

    # Method to be overridden by child classes, defines a single round of the game
    def play_round(self):
        pass

    # Display final game stats after the player finishes playing
    def final_stats(self):
        print(
            f"Final stats - Wins: {self.wins}, Losses: {self.losses}, Draws: {self.draws}."
        )

    # Core game loop where rounds are played, and stats are shown at the end
    def run_game(self):
        self.greet()
        while True:
            self.play_round()
            if not get_yes_no_input("Play again? (y/n): "):
                break
        self.final_stats()


# Class for the Rock Paper Scissors game, extends the base Game class
class RockPaperScissorsGame(Game):
    def __init__(self):
        super().__init__(list_of_games[0])
        self.hands = ("Rock", "Paper", "Scissors")

    # Private method to generate the computer's choice randomly
    def __computer_hand_choice(self):
        return random.randint(0, 2)

    # Private method to update game result based on player's and computer's hands
    def __update_game_result(self):
        if self.players_hand == self.computer_hand:
            self.draws += 1
            print("Draw")
        elif (self.players_hand - self.computer_hand) % 3 == 1:
            self.wins += 1
            print("You win")
        else:
            self.losses += 1
            print("You lose")

    # Static method to get the player's choice as Rock, Paper, or Scissors
    @staticmethod
    def __player_hand_choice():
        while True:
            player_input = input("Rock, paper, or scissors? (r/p/s): ").strip().lower()
            if player_input == "r":
                return 0
            elif player_input == "p":
                return 1
            elif player_input == "s":
                return 2
            else:
                print("Invalid choice! Please choose r, p, or s.")

    # Method to play one round of Rock Paper Scissors
    def play_round(self):
        self.players_hand = self.__player_hand_choice()
        self.computer_hand = self.__computer_hand_choice()
        print(f"Your hand: {self.hands[self.players_hand]}")
        print(f"Computer's hand: {self.hands[self.computer_hand]}")
        self.__update_game_result()


# Class for the Number Guessing Game, extends the base Game class
class NumberGuessingGame(Game):
    def __init__(self):
        super().__init__(list_of_games[1])
        self.lowest_number = LOWEST_GUESS_NUMBER
        self.highest_number = HIGHEST_GUESS_NUMBER
        self.number_of_guesses_left = NUMBER_OF_GUESSES

    # Overridden method to display stats without "draws"
    def final_stats(self):
        print(f"Final stats - Wins: {self.wins}, Losses: {self.losses}.")

    # Private method to generate a target number for the game
    def __generate_target_number(self):
        return random.randint(self.lowest_number, self.highest_number)

    # Private method to check if the player's guess matches the target number
    def __check_number(self, guess, target_number):
        if guess == target_number:
            print("Correct! You win.")
            self.wins += 1
            return True
        elif guess < target_number:
            print("Too low!")
        else:
            print("Too high!")
        return False

    # Method to play one round of the Number Guessing Game
    def play_round(self):
        self.number_of_guesses_left = NUMBER_OF_GUESSES
        target_number = self.__generate_target_number()
        print(
            f"I hold a number between {self.lowest_number} and {self.highest_number}."
        )

        while self.number_of_guesses_left > 0:
            guess_input = (
                input(
                    f"({self.number_of_guesses_left} attempts left.) Take a guess (q to quit): "
                )
                .strip()
                .lower()
            )

            if guess_input == "q":
                break

            if guess_input.isdigit():
                guess = int(guess_input)
                if guess < self.lowest_number or guess > self.highest_number:
                    print(
                        f"Please enter a number between {self.lowest_number} and {self.highest_number}."
                    )
                else:
                    self.number_of_guesses_left -= 1
                    if self.__check_number(guess, target_number):
                        break
            else:
                print("Invalid input. Please enter a valid number.")

            if self.number_of_guesses_left == 0:
                self.losses += 1
                print(
                    f"Sorry, you are out of attempts. The correct number was {target_number}. You lose!"
                )


# Class for the Dice Rolling Game, extends the base Game class
class DiceRollingGame(Game):
    def __init__(self):
        super().__init__(list_of_games[2])
        self.highest_dice_value = HIGHEST_DICE_VALUE

    # Method to roll a dice and return a random value
    def roll_dice(self):
        return random.randint(1, self.highest_dice_value)

    # Method to play one round of the Dice Rolling Game
    def play_round(self):
        self.players_dice_value = self.roll_dice()
        self.computer_dice_value = self.roll_dice()
        print(f"Your dice roll: {self.players_dice_value}")
        print(f"Computer's dice roll: {self.computer_dice_value}")
        if self.players_dice_value > self.computer_dice_value:
            print("You win!")
            self.wins += 1
        elif self.players_dice_value < self.computer_dice_value:
            print("You lose!")
            self.losses += 1
        else:
            print("Draw!")
            self.draws += 1


# Map to associate game names with their respective classes
game_map = {
    list_of_games[0]: RockPaperScissorsGame,
    list_of_games[1]: NumberGuessingGame,
    list_of_games[2]: DiceRollingGame,
}


# Function to allow the user to choose a game from the list
def choose_game(game_map):
    error_message = (
        "Invalid choice! Please enter a valid number corresponding to a game."
    )
    input_message = (
        "Choose a game: "
        + ", ".join(
            [f"({i+1}) {list(game_map.keys())[i]}" for i in range(len(game_map))]
        )
        + ": "
    )

    while True:
        try:
            game_choice = int(input(input_message).strip())
            if 1 <= game_choice <= len(game_map):
                selected_game_class = list(game_map.values())[game_choice - 1]
                return selected_game_class()
        except ValueError:
            pass
        print(error_message)


# Main function to run the gaming platform
def main():
    print("Welcome to my gaming platform!")
    while True:
        game = choose_game(game_map)
        game.run_game()
        if not get_yes_no_input("Play another game? (y/n): "):
            break
    print("Thanks for playing! Come again soon!")


# If the script is run directly, call the main function
if __name__ == "__main__":
    main()
