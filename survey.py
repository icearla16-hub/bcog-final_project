# Constants
question_file = "questions.txt"
answer_options_file = (
    "answer_options.csv"  # Three answer options are given per question.
)
response_file = "responses.txt"  # A response is the answer option the user chooses.


def get_question(question_file):
    question_list = []
    with open(question_file, "r") as fh:
        for line in fh:
            question = line.strip()
            question_list.append(question)
    return question_list


def get_answer_options(answer_options_file):
    answer_options_list = []
    with open(answer_options_file, "r") as fh:
        for line in fh:
            answer_options = line.strip("\n").split(",,")
            answer_options_list.append(answer_options)
    return answer_options_list


def ask_question(question_list, answer_options_list, num: int):
    for i, question in enumerate(question_list):
        print(question_list[num])
        print(answer_options_list[num])
        response = input(str("Select your answer: "))
        num += 1
        if response not in ["a", "b", "c"]:
            raise ValueError("Please enter 'a', 'b', or 'c'.")
        return response


def save_answers(response):
    with open(response_file, "a") as file:
        file.write(f"{response}\n")


def main():
    for i in range(7):
        num = 2
        question_list = get_question(question_file)
        answer_options_list = get_answer_options(answer_options_file)
        ask_question(question_list, answer_options_list, num)
        num = 4


if __name__ == "__main__":
    main()
