import os
from typing import List

aoc_day_num = 2

input_file = os.path.join(os.path.dirname(__file__), f'day{aoc_day_num:02}.txt')


def line_to_pair(l: str) -> List[str]:
    return l.strip().split(' ')


sample_guide = list()
for line in ["A Y", "B X", "C Z"]:
    play, response = line_to_pair(line)
    sample_guide.append((play, response))

strategy_guide = list()
with open(input_file, 'r') as inp:
    for line in inp:
        play, response = line_to_pair(line)
        strategy_guide.append((play, response))
