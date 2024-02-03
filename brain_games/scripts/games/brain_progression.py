import random
from brain_games.scripts import testing
from brain_games.scripts import greetings


def main():

    def cycle(count):
        first_number = random.randint(1, 100)
        interval = random.randint(1, 10)
        progression = [first_number]
        for n in range(random.randint(5, 10)):
            progression.append(progression[-1] + interval)
        index = random.randint(1, len(progression) - 1)
        correct_answer = str(progression[index])
        progression[index] = '..'
        progression = ' '.join(list(map(str, progression)))
        result = testing.test(progression, correct_answer, count, name)
        if result:
            cycle(count - 1)

    name = greetings.greeting()
    print('What number is missing in the progression?')
    cycle(3)


if __name__ == '__main__':
    main()
