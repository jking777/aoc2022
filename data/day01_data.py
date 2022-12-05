import os

aoc_day_num = 1

sample_file = os.path.join(os.path.dirname(__file__), f'day{aoc_day_num:02}_sample.txt')
input_file = os.path.join(os.path.dirname(__file__), f'day{aoc_day_num:02}.txt')

with open(sample_file, 'r') as inp:
    sample_lines = inp.read().splitlines()

with open(input_file, 'r') as inp:
    input_lines = inp.read().splitlines()
