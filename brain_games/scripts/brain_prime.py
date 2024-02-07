#!/usr/bin/env python3

from brain_games.games.prime import prime_test
from brain_games.games.gameplay import game_process

question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    game_process(prime_test, question)


if __name__ == '__main__':
    main()
