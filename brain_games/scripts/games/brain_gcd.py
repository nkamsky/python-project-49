import random
from brain_games.scripts import testing
from brain_games.scripts import greetings


def main():

    def cycle(count):
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
            cycle(count - 1)

    name = greetings.greeting()
    print('Find the greatest common divisor of given numbers.')
    cycle(3)


if __name__ == '__main__':
    main()
