import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]  # Lowercase options to match user input

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input. Please type Rock, Paper, or Scissors.")
        continue

    # Generate random choice for the computer
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    # Check for a tie
    if user_input == computer_pick:
        print("It's a tie!")
    # Check for user win conditions
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        print("You won!")
        user_wins += 1
    # If none of the above, computer wins
    else:
        print("You lost. Computer wins.")
        computer_wins += 1

# Final tally of wins
print(f"\nYou won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print("Goodbye!")
