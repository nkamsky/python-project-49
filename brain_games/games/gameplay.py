import prompt


def game_process(type_of_game, question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    count = 0
    while count < 3:
        print(question)
        test, result = type_of_game()
        print(f'Question: {test}')
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
            count += 1
        else:
            print(f'\'{answer}\' is wrong answer ;(.\n'
                  f'Correct answer was \'{result}\'.\n'
                  f'Let\'s try again, {name}!')
            break
    if count == 3:
        print(f'Congratulations, {name}!')
