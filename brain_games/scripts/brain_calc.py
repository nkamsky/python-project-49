#!/usr/bin/env python3

from brain_games.games.calc import calculation_test
from brain_games.games.gameplay import game_process

question = 'What is the result of the expression?'


def main():
    game_process(calculation_test, question)


if __name__ == '__main__':
    main()
