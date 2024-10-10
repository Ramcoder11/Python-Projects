import random

# Ask for a valid number until the user provides one
while True:
    max_range = input("Type a number: ")

    # Check if input is a valid positive integer
    if max_range.isdigit():
        max_range = int(max_range)
        if max_range > 0:  # Ensure the number is larger than 0
            break
        else:
            print("Please type a number larger than 0.")
    else:
        print("Invalid input. Please type a valid number.")

# Generate a random number between 1 and the max range
random_number = random.randint(1, max_range)
guesses = 0

# Main game loop
while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    # Check if the user's input is a digit
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a valid number.")
        continue

    # Compare user guess with random number
    if user_guess == random_number:
        print("Right answer!")
        break
    elif user_guess > max_range:
        print("You are out of range!!")
        print(f"Guess a number between the range of {1} and {max_range}.")
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

# Display the number of guesses made
print(f"You got it in {guesses} guesses!")
