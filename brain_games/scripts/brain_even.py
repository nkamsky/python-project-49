#!/usr/bin/env python3

from brain_games.games.even import even_test
from brain_games.games.gameplay import game_process

question = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    game_process(even_test, question)


if __name__ == '__main__':
    main()
