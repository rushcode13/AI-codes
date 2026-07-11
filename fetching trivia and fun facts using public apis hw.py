# Import the requests module to fetch data from an online API
import requests

# Import random to shuffle the answer options
import random

# Import html to convert HTML entities into normal text
import html

# Category ID 19 represents Mathematics in the Open Trivia Database
MATH_CATEGORY_ID = 19

# API URL to fetch 10 multiple-choice math questions
API_URL = f"https://opentdb.com/api.php?amount=10&category={MATH_CATEGORY_ID}&type=multiple"

# Function to fetch math questions from the API
def get_math_questions():

    # Send a GET request to the API
    response = requests.get(API_URL)

    # Check if the request was successful
    if response.status_code == 200:

        # Convert the response into a Python dictionary
        data = response.json()

        # Return the list of questions if the API response is valid
        if data["response_code"] == 0 and data["results"]:
            return data["results"]

    # Return None if the request fails
    return None


# Function to run the quiz
def run_quiz():

    # Get the math questions
    questions = get_math_questions()

    # Stop the program if questions could not be fetched
    if not questions:
        print("Failed to fetch math questions.")
        return

    # Variable to store the user's score
    score = 0

    # Display the welcome message
    print("Welcome to the Math Quiz!")

    # Loop through each question
    for i, q in enumerate(questions, 1):

        # Convert HTML symbols into readable text
        question = html.unescape(q["question"])

        # Store the correct answer
        correct = html.unescape(q["correct_answer"])

        # Store all incorrect answers
        incorrects = [html.unescape(ans) for ans in q["incorrect_answers"]]

        # Combine all answer choices
        options = incorrects + [correct]

        # Shuffle the options so the correct answer is in a random position
        random.shuffle(options)

        # Display the question
        print(f"\nQuestion {i}: {question}")

        # Display all answer choices
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        # Keep asking until the user enters a valid option
        while True:
            try:
                choice = int(input("Your answer (1-4): "))

                # Check that the entered number is between 1 and 4
                if 1 <= choice <= 4:
                    break

            except ValueError:
                pass

            print("Invalid input. Please enter a number from 1 to 4.")

        # Check whether the selected answer is correct
        if options[choice - 1] == correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct}")

    # Display the final score
    print(f"\nFinal Score: {score}/{len(questions)}")

    # Calculate and display the percentage
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.1f}%")

    # Display a message based on the user's performance
    if percentage >= 80:
        print("Excellent work!")
    elif percentage >= 60:
        print("Good job!")
    else:
        print("Keep practicing math!")


# Start the quiz only when this file is run directly
if __name__ == "__main__":
    run_quiz()