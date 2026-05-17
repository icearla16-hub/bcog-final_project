# Constants
question_file = "questions.txt"
answer_options_file = "answer_options.csv"
answer_file = "responses.txt"

# Import .py file with the buttons
import display


def get_question(question_file):
    question_list = []
    with open(question_file, "r") as fh:
        for line in fh:
            question = line.strip()
            if question and not question.startswith("###"):
                question_list.append(question)
    return question_list


def get_answer_options(answer_options_file):
    with open(answer_options_file, "r") as fh:
        for line in fh:
            answer_option = line.strip("\n").split(",")
            answer_options_list = [answer_option for line in fh]
        print(answer_options_list)


def ask_question(question_list):
    for i in range(len(question_list)):
        print(question_list[i])
        return input(str("Select your answer: "))


def save_answers(answer):
    with open(answer_file, "a") as file:
        file.write(f"{answer}\n")


def main():
    question_list = get_question(question_file)
    ask_question(question_list)


if __name__ == "__main__":
    main()
    # answer options to csv and questions from question.text
