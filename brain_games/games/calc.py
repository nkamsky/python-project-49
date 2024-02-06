#!/usr/bin/env python3

import random
from brain_games.games import testing
from brain_games.games import greetings


def calculation_test(count):
    operator = random.choice((' + ', ' - ', ' * '))
    number1, number2 = random.randint(1, 10), random.randint(1, 10)
    if operator == ' + ':
        result = str(number1 + number2)
        expression = f'{number1} + {number2}'
    elif operator == ' - ':
        result = str(number1 - number2)
        expression = f'{number1} - {number2}'
    else:
        result = str(number1 * number2)
        expression = f'{number1} * {number2}'
    result = testing.test(expression, result, count, name)
    if result:
        calculation_test(count - 1)


name = greetings.greeting()
print('What is the result of the expression?')
