
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
        gd_1 = []
        for number in range(1, number_1):
            if number_1 % number == 0:
                gd_1.append(number)
        gd_2 = []
        for number in range(1, number_2):
            if number_2 % number == 0:
                gd_2.append(number)
        correct_answer = ''
        for number in reversed(gd_1):
            if number in gd_2:
                correct_answer = str(number)
                break
        result = testing.test(expression, correct_answer, name)
        if result != correct_answer:
            break
        count += 1
        if count == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
