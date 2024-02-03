import random
from brain_games.scripts import testing
from brain_games.scripts import greetings


def main():

    def cycle(count):
        number = random.randint(1, 100)
        if number == 1:
            correct_answer = 'no'
        else:
            i = 0
            for n in range(1, number + 1):
                if number % n == 0:
                    i += 1
            correct_answer = 'no' if i > 2 else 'yes'
        result = testing.test(number, correct_answer, count, name)
        if result:
            cycle(count - 1)

    name = greetings.greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    cycle(3)


if __name__ == '__main__':
    main()
