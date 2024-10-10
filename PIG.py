import random


def roll():
    """Simulates rolling a die (1 to 6)."""
    return random.randint(1, 6)


# Get number of players
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid input. Try again.")

# Game variables
max_score = 20
player_scores = [0 for _ in range(players)]  # Initialize scores for each player

# Main game loop
game_over = False
while not game_over:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn!")
        print(f"Your total score is: {player_scores[player_idx]}\n")  # Show player's total score

        current_score = 0  # This is the score for this turn only

        # Player's turn to roll
        while True:
            should_roll = input("Would you like to roll (y/n)? ").lower()
            if should_roll != 'y':  # Player chooses to stop rolling
                break

            value = roll()  # Roll the die
            if value == 1:
                print("You rolled a 1! Your turn is over, and you lose your points for this turn.")
                current_score = 0  # Lose all points for this turn
                break  # End the turn immediately
            else:
                current_score += value  # Add roll value to current turn's score
                print(f"You rolled a {value}. Current score for this turn: {current_score}")

        # Update the player's total score
        player_scores[player_idx] += current_score  # Add turn's score to total score
        print(f"Player {player_idx + 1}'s total score is now: {player_scores[player_idx]}")

        # Check if the player has won
        if player_scores[player_idx] >= max_score:
            print(f"\nPlayer {player_idx + 1} has won with a score of {player_scores[player_idx]}!")
            game_over = True  # End the game
            break
