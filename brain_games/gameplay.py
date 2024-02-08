import prompt


def game_process(type_of_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(type_of_game.question)
    for _ in range(3):
        test, result = type_of_game.test()
        print(f'Question: {test}')
        answer = prompt.string('Your answer: ')
        if answer != result:
            print(f'\'{answer}\' is wrong answer ;(.\n'
                  f'Correct answer was \'{result}\'.\n'
                  f'Let\'s try again, {name}!')
            break
        else:
            print('Correct!')
        print(f'Congratulations, {name}!')
