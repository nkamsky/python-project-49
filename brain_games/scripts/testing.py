import prompt


def test(expression, correct_answer):
    print(f'Question: {expression}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return 1
    else:
        print(f'\'{answer}\' is wrong answer ;(.\
 Correct answer was \'{correct_answer}\'.')
        return 4
