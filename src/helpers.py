from sys import exit
def get_valid_input(message):
    """
    Prompts the user for input until a valid number of questions is provided.
    Valid input is an integer between 5 and 20, or an empty input which defaults to 10.

    Args:
        message (str): The message to display to the user.

    Returns:
        int: The validated number of questions for the quiz.
    """
    print(message)
    while True:
        try:
            total_questions = input(">> ")  # Get user input
            if total_questions == "":
                return 10  # Default value if no input is provided
            total_questions = int(total_questions)  # Convert input to integer
            if 5 <= total_questions <= 20:
                return total_questions  # Return valid input
            else:
                print("Please enter a number between 5 and 20.")  # Prompt for valid range
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  # Handle non-integer input

def check_answer(user_ans, selected_questions, i, user_score):
    # Check if the answer is correct
    if user_ans == selected_questions[i][5]:
        print("Correct Answer!\n")
        user_score += 1  # Increment score for correct answer
    elif user_ans in ['a', 'b', 'c', 'd']:
        print("Wrong Answer!\n")  # Notify user of wrong answer
    elif user_ans == 'q':
        display_result(user_score, len(selected_questions))
        exit(0)  # Exit the quiz if user chooses to quit
    else:
        print("Invalid Input!")  # Handle invalid input
    return user_score


def display_result(user_score, total_no_of_ques):
    # Display the final score and accuracy
    print(f"\nYou scored: {user_score}/{total_no_of_ques}.\n"
          f"Your accuracy: {user_score / total_no_of_ques * 100:.2f}%.\n")  # Format accuracy to two decimal places
    print("Thanks for playing!")


