# Constants
question_file = "questions.txt"
answer_options_file = "answer_options.csv"
response_file = "responses.txt"  # A response is the answer option the user chooses.


def get_question(question_file):
    question_list = []
    with open(question_file, "r") as fh:
        for line in fh:
            question = line.strip()
            if question and not question.startswith("###"):
                question_list.append(question)
    return question_list


def get_answer_options(answer_options_file):
    answer_options_list = []
    with open(answer_options_file, "r") as fh:
        for line in fh:
            answer_option = line.strip("\n").split(",")
            answer_options_list.append(answer_option)
    print(answer_options_list)


def ask_question(question_list):
    for question in question_list:
        print(question)
        response = input(str("Select your answer: "))
        return response


def save_answers(response):
    with open(response_file, "a") as file:
        file.write(f"{response}\n")


def main():
    question_list = get_question(question_file)
    get_answer_options(answer_options_file)
    ask_question(question_list)


if __name__ == "__main__":
    main()
