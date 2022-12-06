from data.day02_data import sample_guide, strategy_guide

sample = False
if sample:
    guide = sample_guide
else:
    guide = strategy_guide

scores = {'X': 1, 'Y': 2, 'Z': 3}

lose = 0
draw = 3
win = 6

outcomes = {
    'X': {
        'A': draw,
        'B': lose,
        'C': win
    },
    'Y': {
        'A': win,
        'B': draw,
        'C': lose
    },
    'Z': {
        'A': lose,
        'B': win,
        'C': draw
    }
}


def part1():
    total_score = 0
    for play, response in guide:
        total_score += scores[response]
        total_score += outcomes[response][play]

    print(f"Part 1 total score:  {total_score}")


def part2():
    lose_responses = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    draw_responses = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    win_responses = {'A': 'Y', 'B': 'Z', 'C': 'X'}

    total_score = 0
    for play, outcome in guide:
        if outcome == 'X':
            response = lose_responses[play]
            # no addition to score for a loss
        elif outcome == 'Y':
            # draw
            response = draw_responses[play]
            total_score += 3
        elif outcome == 'Z':
            # win
            response = win_responses[play]
            total_score += 6
        else:
            print(f"Unknown outcome code:  {outcome}")
        total_score += scores[response]

    print(f"Part 2 total score:  {total_score}")


if __name__ == "__main__":
    part1()
    part2()
