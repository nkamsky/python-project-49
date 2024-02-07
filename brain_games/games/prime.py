import random


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def prime_test():
    number = random.randint(1, 100)
    prime = is_prime(number)
    result = 'yes' if prime else 'no'
    return number, result
