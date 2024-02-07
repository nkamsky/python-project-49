#!/usr/bin/env python3

from brain_games.games.progression import find_num_in_progression
from brain_games.games.gameplay import game_process

question = 'What number is missing in the progression?'


def main():
    game_process(find_num_in_progression, question)


if __name__ == '__main__':
    main()
