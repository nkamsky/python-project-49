import random

question = 'Answer "yes" if the number is even, otherwise answer "no".'


def test():
    number = random.randint(0, 100)
    result = 'yes' if number % 2 == 0 else 'no'
    return number, result
