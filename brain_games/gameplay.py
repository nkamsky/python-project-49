import prompt

ROUNDS_COUNT = 3


def game_process(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.INSTRUCTION)
    for _ in range(ROUNDS_COUNT):
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
