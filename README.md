# QuizPy

QuizPy is a simple and interactive quiz application built in Python. It allows users to test their knowledge across various topics by answering multiple-choice questions. The application randomly selects questions from a predefined list and calculates the user's score based on their answers.

## Features

- **Randomized Questions**: Each quiz session presents a random selection of questions.
- **User-Friendly Interface**: Simple command-line interface for easy navigation.
- **Score Calculation**: Displays the user's score and accuracy at the end of the quiz.
- **Quit Option**: Users can exit the quiz at any time by typing 'q'.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/koushikkundu/quizpy.git
   cd quizpy
   ```

2. Ensure you have the necessary files:
   - `main.py`: The entry point of the application.
   - `helpers.py`: Contains helper functions for input validation and score calculation.
   - `questions.py`: Contains a list of all questions and answers.
   - `__init__.py`: An empty file to mark the directory as a package.

### Running the Application

To start the quiz application, run the following command in your terminal:

```bash
python main.py
```

Follow the prompts to begin the quiz. You can choose the number of questions (between 5 and 20) or press Enter to use the default of 10 questions.

### Example Interaction

```
Welcome to the QuizPy!
Would you like to start? (y/n)
>> y
Enter the number of questions for the quiz (5 to 20).
(Press Enter for default.)
>> 
You can answer the questions by typing 'a', 'b', 'c', or 'd'.
Type 'q' at any time to quit the quiz.

Q.1: What is the capital of France?
a) Berlin
b) Madrid
c) Paris
d) Lisbon
Your answer (a/b/c/d) >> c
Correct Answer!

...
You scored: 8/10.
Your accuracy: 80.00%.
Thanks for playing!
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all the contributors and users who help improve this project.
- Special thanks to the creators of the questions used in this quiz.
