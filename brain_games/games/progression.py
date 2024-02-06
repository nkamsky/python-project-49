#!/usr/bin/env python3

import random
from brain_games.games import testing
from brain_games.games import greetings


def find_num_in_progression(count):
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    num_of_elements = random.randint(5, 10)
    progression = list(range(start, start + step * num_of_elements, step))
    index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[index])
    progression[index] = '..'
    progression = ' '.join(list(map(str, progression)))
    result = testing.test(progression, correct_answer, count, name)
    if result:
        find_num_in_progression(count - 1)


name = greetings.greeting()
print('What number is missing in the progression?')
