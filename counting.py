answer_file = 'responses.txt'

def count(file_path):
    counts = {'a':0, 'b':0, 'c':0}

    with open(file_path, 'r') as fh:
        for line in fh:
            letter = line.strip().lower()
            if letter in counts:
                counts[letter] += 1
    return counts

def specific_personality(counts):
    a,b,c = counts['a'], counts['b'], counts['c']
    if a > b and a > c:
        return 'A personality classification find from text'
    elif b > a and b > c:
        return 'b personality classification find from text'
    else:
        return 'c personality classification find from text'

def ties(counts):
    a,b,c = counts['a'], counts['b'], counts['c']
    max_value = max(a,b,c)
    winners = [letter for letter, count in counts.items() if count == max_value]
    if len(winners) > 1:
        tie = {'a': 'a type thing in notes', 'b': 'b type thing in notes', 'c': 'c type thing in notes'}
        results_for_tie = [tie[i] for i in winners]
        return f'Based on the choices you have made in your path, we believe you are a mix of two personalities. We believe you are both {results_for_tie[0]} and {results_for_tie[1]}! We hope these test results let you understand more about who you are and the decisions you tend to make. (maybe add more text here)'
    return None

def results():
    data = count(answer_file)
    checking_if_tie = ties(data)
    if checking_if_tie:
        print(checking_if_tie)
    else:
        personality = specific_personality(data)
    print(f'Based on the choices you have made you align most similar to {personality}!')
    print('This means you tend to make chocies to that blah balh finish!')


if __name__ == '__main__':
    results()