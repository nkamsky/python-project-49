#!/usr/bin/env python3

import random
from brain_games.games import testing
from brain_games.games import greetings


def even_test(count):
    random_number = random.randint(0, 100)
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    result = testing.test(random_number, correct_answer, count, name)
    if result:
        even_test(count - 1)


name = greetings.greeting()
print('Answer "yes" if the number is even, otherwise answer "no".')
