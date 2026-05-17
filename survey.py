# Constants
question_file = "questions.txt"
answer_options_file = (
    "answer_options.csv"  # Three answer options are given per question.
)
response_file = "responses.txt"  # A response is the answer option the user chooses.


def get_question(question_file):
    with open(question_file, "r") as fh:
        for line in fh:
            question = line.strip()
            question_list = [question for line in fh]
    return question_list


def get_answer_options(answer_options_file):
    with open(answer_options_file, "r") as fh:
        for line in fh:
            answer_options = line.strip("\n").split(",")
            answer_options_list = [answer_options for line in fh]
    print(answer_options_list)
    return answer_options_list


def ask_question(question_list, answer_options_list):
    for question in question_list:
        print(question)
    for answer_options in answer_options_list:
        print(answer_options)
        response = input(str("Select your answer: "))
        return response


def save_answers(response):
    with open(response_file, "a") as file:
        file.write(f"{response}\n")


def main():
    question_list = get_question(question_file)
    answer_options_list = get_answer_options(answer_options_file)
    ask_question(question_list, answer_options_list)


if __name__ == "__main__":
    main()
