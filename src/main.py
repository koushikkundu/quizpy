import random
from src.questions import all_questions
from src.helpers import *

def main():
    """
    Main function to start the quiz application.
    Prompts the user to start the quiz or exit.
    """
    while True:
        selected_option = input(">> ")  # Prompt for starting the quiz

        if selected_option == 'y':
            begin_quiz()  # Start the quiz if user agrees
            exit(0)
        elif selected_option == 'n':
            print("Thank you for visiting! See you next time!")  # Exit message
            exit(0)
        else:
            print("Oops! That's not a valid option. Please enter 'y' or 'n'.")  # Handle invalid input


def begin_quiz():
    """
    Starts the quiz, handles the quiz logic, and calculates the score.
    """
    user_score = 0  # Initialize score

    # Get the number of questions for the quiz
    total_no_of_ques = get_valid_input("Enter the number of questions for the quiz (5 to 20).\n"
                                       "(Press Enter for default.)")

    # Randomly select questions from the available questions
    selected_questions = random.sample(all_questions, total_no_of_ques)

    print("\nYou can answer the questions by typing 'a', 'b', 'c', or 'd'.\n"
          "Type 'q' at any time to quit the quiz.\n")

    # Loop through the selected questions
    for i in range(total_no_of_ques):
        # Display the question and answer options
        user_ans = input(f"Q.{i + 1}: {selected_questions[i][0]}\n"
                    f"a) {selected_questions[i][1]}\n"
                    f"b) {selected_questions[i][2]}\n"
                    f"c) {selected_questions[i][3]}\n"
                    f"d) {selected_questions[i][4]}\n"
                    "Your answer (a/b/c/d) >> ").lower()  # Convert input to lowercase for consistency

        # Check if the answer is correct
        user_score = check_answer(user_ans, selected_questions, i, user_score)

    display_result(user_score, total_no_of_ques) # Display the result


if __name__ == "__main__":
    print("Welcome to the QuizPy!")  # Welcome message
    print("Would you like to start? (y/n)") # Start prompt
    main()  # Entry point of the program
