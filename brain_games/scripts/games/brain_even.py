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
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        count += testing.test(random_number, correct_answer)
    print(f'Congratulations, {name}!') if count == 3 \
        else print(f'Let\'s try again, {name}!')


if __name__ == '__main__':
    main()
