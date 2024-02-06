#!/usr/bin/env python3

import random
from brain_games.games import testing
from brain_games.games import greetings


def gcd_test(count):
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    expression = f'{number_1} {number_2}'
    correct_answer = ''
    for n in range(number_1, 0, -1):
        if number_1 % n == 0:
            if number_2 % n == 0:
                correct_answer = str(n)
                break
    result = testing.test(expression, correct_answer, count, name)
    if result:
        gcd_test(count - 1)


name = greetings.greeting()
print('Find the greatest common divisor of given numbers.')
