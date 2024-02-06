#!/usr/bin/env python3

import random
from brain_games.games import testing
from brain_games.games import greetings


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def prime_test(count):
    number = random.randint(1, 100)
    prime = is_prime(number)
    correct_answer = 'yes' if prime else 'no'
    result = testing.test(number, correct_answer, count, name)
    if result:
        prime_test(count - 1)


name = greetings.greeting()
print('Answer "yes" if given number is prime. Otherwise answer "no".')
