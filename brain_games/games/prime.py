import random

question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
        return True


def test():
    number = random.randint(1, 100)
    result = 'yes' if is_prime(number) else 'no'
    return number, result
