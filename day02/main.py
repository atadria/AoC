# https://adventofcode.com/2021/day/2

INPUT_PATH = 'input.txt'


def part1(data):
    h = 0
    v = 0
    for c, p in data:
        if c == 'up':
            v -= p
        elif c == 'down':
            v += p
        else:
            h += p
    print(v * h)


def part2(data):
    """
    * down X increases your aim by X units.
    * up X decreases your aim by X units.
    * forward X does two things:
        - It increases your horizontal position by X units.
        - It increases your depth by your aim multiplied by X.
    """
    aim = 0
    h = 0
    d = 0
    for c, p in data:
        if c == 'up':
            aim -= p
        elif c == 'down':
            aim += p
        else:
            h += p
            d += aim * p
    print(d * h)


if __name__ == '__main__':
    input_data = []
    for line in open(INPUT_PATH, 'r'):
        c, p = line.strip().split()
        input_data.append((c.strip(), int(p)))

    part1(input_data)
    part2(input_data)
