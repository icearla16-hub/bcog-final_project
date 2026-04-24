# Constants
question_file = "questions.txt"

# Imports
import tkinter as tk

root = tk.Tk()

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
    return input("Enter your answer (a/b/c): ")
    # make this a button (?)

def calculate_score(response_txt):
    pass

def main():
    get_question(question_file)
    return True


if __name__ == "__main__":
    main()
    # answer options to csv and questions from question.text
