import prompt


def test(expression, correct_answer, name):
    print(f'Question: {expression}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return answer
    else:
        print(f'{answer} is wrong answer ;(.\
 Correct answer was {correct_answer}.')
        print(f'Let\'s try again, {name}')
        return answer
