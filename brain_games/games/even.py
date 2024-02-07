import random


def even_test():
    number = random.randint(0, 100)
    result = 'yes' if number % 2 == 0 else 'no'
    return number, result
