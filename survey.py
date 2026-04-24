# Constants
question_file = "questions.txt"
answer_options = "answer_options.csv"

# Import .py file with the buttons
import display

def get_question(question_file):
    question_list = []
    with open(question_file, "r") as fh:
        for question in fh:
            question = question.strip().split(",")
            question_text = question[0]
            letter = question[1]
            question_list.append((question_text, letter))
    return question_list


def ask_question(question):
    print(question[0])
    return input("Select your answer: ")

# def calculate_score(response_txt):
#    pass

def save_answers():
    answer_list = []

def main():
    get_question(question_file)
    return True


if __name__ == "__main__":
    main()
    # answer options to csv and questions from question.text
