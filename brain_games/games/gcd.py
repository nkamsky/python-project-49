import random
import math

INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def get_task_and_result():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    two_numbers = f'{number_1} {number_2}'
    result = str(math.gcd(number_1, number_2))
    return two_numbers, result
