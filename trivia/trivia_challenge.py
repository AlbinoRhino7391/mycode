import requests

def get_trivia_questions(num_questions, category, difficulty, question_type):
    BASE_URL = "https://opentdb.com/api.php"

    # Prepare the parameters for the API request
    params = {
        "amount": num_questions,
        "category": category,
        "difficulty": difficulty,
        "type": question_type,
        "encode": "url3986",  # Default Encoding
    }

    # Send the API request
    response = requests.get(BASE_URL, params=params)

    # Decode the response JSON
    data = response.json()

    return data.get("results", [])

def print_trivia_questions(questions):
    for i, question_data in enumerate(questions, 1):
        question = requests.utils.unquote(question_data["question"])
        answers = [requests.utils.unquote(ans) for ans in question_data["incorrect_answers"]]
        correct_answer = requests.utils.unquote(question_data["correct_answer"])
        answers.append(correct_answer)
        # Shuffle the answers so that correct answer doesn't always appear last
        import random
        random.shuffle(answers)

        print(f"\nQuestion {i}: {question}")
        print("Answers:")
        for j, ans in enumerate(answers, 1):
            print(f"{j}. {ans}")

        # Take user input for their answer
        user_input = input("Enter the number of your answer: ")

        # Check if the input is valid
        if not user_input.isdigit() or not 1 <= int(user_input) <= len(answers):
            print("Invalid input. Please enter a valid option.")
            continue

        # Check if the user's answer is correct
        user_answer = answers[int(user_input) - 1]
        if user_answer == correct_answer:
            print("Correct answer!")
        else:
            print(f"Wrong answer. The correct answer is: {correct_answer}")

if __name__ == "__main__":
    # Your specifications
    num_questions = 3
    category = 9  # You choose the category (e.g., General Knowledge, category 9)
    difficulty = "easy"  # You choose the difficulty (easy, medium, hard)
    question_type = "multiple"  # You choose the type (multiple choice, true/false)

    # Get trivia questions
    trivia_questions = get_trivia_questions(num_questions, category, difficulty, question_type)

    # Print the questions and take user input for answers
    print_trivia_questions(trivia_questions)
