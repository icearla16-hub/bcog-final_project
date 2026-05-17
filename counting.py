response_file = "responses.txt"


def count(file_path):
    counts = {"a": 0, "b": 0, "c": 0}

    with open(file_path, "r") as fh:
        for line in fh:
            letter = line.strip().lower()
            if letter in counts:
                counts[letter] += 1
    return counts


def specific_personality(counts):
    a, b, c = counts["a"], counts["b"], counts["c"]
    if a > b and a > c:
        return "You are the A personality. This personality means that despite the possibility of being harmed, you always choose to help."
    elif b > a and b > c:
        return "You are the B personality. This personality means that you are a practical person who chooses to help when it does not hurt you, but you will not go out of your way to help."
    else:
        return "You are the C personality. This personality means that you are a focused person, reliant on only your skills to reach your goals."


def ties(counts):
    a, b, c = counts["a"], counts["b"], counts["c"]
    max_value = max(a, b, c)
    winners = [letter for letter, count in counts.items() if count == max_value]
    if len(winners) > 1:
        tie = {
            "a": "A personality, this personality means that despite the possibility of being harmed, you always choose to help,",
            "b": "B personality, this personality means that you are a practical person who chooses to help when it does not hurt you, but you will not go out of your way to help,",
            "c": "C personality, this personality means that you are a focused person, reliant on only your skills to reach your goals,",
        }
        results_for_tie = [tie[i] for i in winners]
        return f"Based on the choices you have made in your path, we believe you are a mix of two personalities. We believe you are both {results_for_tie[0]} and {results_for_tie[1]}! We hope these test results let you understand more about who you are and the decisions you tend to make. Thanks for playing our game!"
    return None


def results():
    data = count(response_file)
    checking_if_tie = ties(data)
    if checking_if_tie:
        print(checking_if_tie)
    else:
        personality = specific_personality(data)
        print(f"Based on the choices you have made you align most similar to:")
        print(personality)
        print(
            "We hope these test results let you understand more about who you are and the decisions you tend to make. Thanks for playing our game!"
        )


if __name__ == "__main__":
    results()
