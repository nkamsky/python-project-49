import random
import math

INSTRUCTION = ('Answer "yes" if given number is prime. '
               'Otherwise answer "no".')


def is_prime(x):
    if x < 2:
        return False
    for n in range(2, int(math.sqrt(x)) + 1):
        if x % n == 0:
            return False
    return True


def get_task_and_result():
    number = random.randint(1, 100)
    result = 'yes' if is_prime(number) else 'no'
    return number, result
