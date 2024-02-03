import prompt
from brain_games.scripts import greetings


def test(expression, correct_answer, count, name):
    print(f'Question: {expression}')
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        if count == 1:
            print(f'Congratulations, {name}!')
        else:
            return True
    else:
        print(f'\'{answer}\' is wrong answer ;(.\
Correct answer was \'{correct_answer}\'.')
        print(f'Let\'s try again, {name}!')
