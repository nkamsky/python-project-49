import random
import prompt
from brain_games.scripts import testing


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        number = random.randint(1, 100)
        i = 0
        for n in range(1, number + 1):
            if number % n == 0:
                i += 1
        correct_answer = 'no' if i > 2 or number == 1 else 'yes'
        count += testing.test(number, correct_answer)
    print(f'Congratulations, {name}!') if count == 3 else print(f'Let\'s try again, {name}')


if __name__ == '__main__':
    main()