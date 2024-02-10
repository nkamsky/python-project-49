import random

INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_task_and_result():
    number = random.randint(0, 100)
    result = 'yes' if number % 2 == 0 else 'no'
    return number, result
