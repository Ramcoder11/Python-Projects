print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    print("Okay, maybe next time!")
    quit()  # To terminate the program

print("\nGreat! Let's play :)")

# Dictionary to store questions as keys and answers as values pair
questions_and_answers = {
    "What does CPU stand for?": "central processing unit",
    "What does GPU stand for?": "graphical processing unit",
    "What does RAM stand for?": "random access memory",
    "What does PSU stand for?": "power supply unit"
}

score = 0

# Loop through the questions and check the answers
for question, correct_answer in questions_and_answers.items():
    answer = input(question + " ").lower()
    if answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"The correct answer is {correct_answer}")
print()

# Final scores
total_questions = len(questions_and_answers)  # Get the total no of questions from the dictionary
print(f"You got {score} out of {total_questions} questions correct!")
percentage = score / total_questions * 100
print(f"Your score is {percentage}%")

