#!/usr/bin/env python3

import random
from brain_games.scripts import testing
from brain_games.scripts import greetings


def main():

    def cycle(count):
        operator = random.choice((' + ', ' - ', ' * '))
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 10)
        expression = str(number_1) + operator + str(number_2)
        correct_answer = str(eval(str(number_1) + operator + str(number_2)))
        result = testing.test(expression, correct_answer, count, name)
        if result:
            cycle(count - 1)

    name = greetings.greeting()
    print('What is the result of the expression?')
    cycle(3)


if __name__ == '__main__':
    main()
