#!/usr/bin/env python3

import prompt
from brain_games.scripts import testing
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        random_number = random.randint(0, 100)
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
            result = testing.test(random_number, correct_answer, name)
            if result != correct_answer:
                break
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
