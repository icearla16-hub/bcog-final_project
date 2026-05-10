# Constants
question_file = "questions.txt"
answer_options = "answer_options.csv"
answer_file = "responses.txt"

# Import .py file with the buttons
import display


def get_question(question_file):
    question_list = []
    with open(question_file, "r") as fh:
        for question in fh:
            question = question.strip()
            if question and not question.startswith("###"):
                question_list.append(question)
    return question_list


def ask_question(question_list):
    for i in range(len(question_list)):
        print(question_list[i])
        return input("Select your answer: ")


def save_answers(answer):
    with open(answer_file, "a") as file:
        file.write(f"{answer}\n")


def main():
    question_list = get_question(question_file)
    ask_question(question_list)


if __name__ == "__main__":
    question_list = get_question(question_file)
    ask_question(question_list)
    main()
    # answer options to csv and questions from question.text
