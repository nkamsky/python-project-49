#!/usr/bin/env python3

import random
import prompt
from brain_games.scripts import testing


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        operator = random.choice((' + ', ' - ', ' * '))
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        expression = str(number_1) + operator + str(number_2)
        correct_answer = str(eval(str(number_1) + operator + str(number_2)))
        result = testing.test(expression, correct_answer, name)
        if result != correct_answer:
            break
        count += 1
        if count == 3:
            print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
