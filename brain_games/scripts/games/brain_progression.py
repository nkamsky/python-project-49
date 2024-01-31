import random
import prompt
from brain_games.scripts import testing


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    count = 0
    while count < 3:
        first_number = random.randint(1, 100)
        interval = random.randint(1, 10)
        progression = [first_number]
        for n in range(random.randint(5, 10)):
            progression.append(progression[-1] + interval)
        index = random.randint(1, len(progression) - 1)
        correct_answer = str(progression[index])
        progression[index] = '..'
        progression = ' '.join(list(map(str, progression)))
        count += testing.test(progression, correct_answer)
    print(f'Congratulations, {name}!') if count == 3 \
        else print(f'Let\'s try again, {name}!')


if __name__ == '__main__':
    main()
