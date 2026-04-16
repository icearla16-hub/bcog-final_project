def main():
    return True

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
    possible_answers = ()
    return True

if __name__ == "__main__":
    main()