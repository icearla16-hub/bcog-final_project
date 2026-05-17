# Constants
question_file = "questions.txt"
answer_options_file = (
    "answer_options.csv"  # Three answer options are given per question.
)
response_file = "responses.txt"  # A response is the answer option the user chooses.

# opening the question file and creating a list of the questions from questions.txt
def get_question(question_file):
    with open(question_file, "r") as fh:
        for line in fh:
            question_list = [line.strip() for line in fh]
    return question_list

# opening the .csv file with the answer options, and saving the options
def get_answer_options(answer_options_file):
    with open(answer_options_file, "r") as fh:
            answer_options_list = [line.strip("\n").split(",,")for line in fh]
    return answer_options_list

def ask_question(question_list, answer_options_list):
    for i in range(len(question_list)):
        print(question_list[i])
        print(answer_options_list[i])
        response = input(str("Select your answer: "))
        if response not in ["A", "B", "C"]:
            raise ValueError("Please enter 'A', 'B', or 'C'.")
        return response

# saving the answers to responses.txt
def save_answers(response):
    with open(response_file, "a") as file:
        file.write(f"{response}\n")

# putting it all together
def main():
    for i in range (len(question_file)):
        question_list = get_question(question_file)
        answer_options_list = get_answer_options(answer_options_file)
        for i in range(len(question_list)): # printing one question + row of answer choices at a time
            print(question_list[i])
            print(answer_options_list[i])
            response = input(str("Select your answer: "))
            if response not in ["A", "B", "C"]:
                raise ValueError("Please enter 'A', 'B', or 'C'.")
        return response
    save_answers(response) 


if __name__ == "__main__":
    main()
