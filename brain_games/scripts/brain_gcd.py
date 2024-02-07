#!/usr/bin/env python3

from brain_games.games.gcd import gcd_test
from brain_games.games.gameplay import game_process

question = 'Find the greatest common divisor of given numbers.'


def main():
    game_process(gcd_test, question)


if __name__ == '__main__':
    main()
