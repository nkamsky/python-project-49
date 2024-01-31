import random
import prompt
from brain_games.scripts import testing


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        expression = f'{number_1} {number_2}'
        correct_answer = ''
        for n in range(number_1, 0, -1):
            if number_1 % n == 0:
                if number_2 % n == 0:
                    correct_answer = str(n)
                    break
        count += testing.test(expression, correct_answer)
    print(f'Congratulations, {name}!') if count == 3 else print(f'Let\'s try again, {name}!')


if __name__ == '__main__':
    main()
