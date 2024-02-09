import prompt
from brain_games import constants


def game_process(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.question)
    for _ in range(constants.REPEAT_CORRECT_ANSWER):
        task, correct_answer = game.get_task_and_result()
        print(f'Question: {task}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(.\n'
                  f'Correct answer was \'{correct_answer}\'.\n'
                  f'Let\'s try again, {name}!')
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
