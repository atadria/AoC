# https://adventofcode.com/2021/day/1

INPUT_PATH = 'input.txt'


def part1(data):
    increase = 0
    last_measurement = None
    for m in data:
        if last_measurement and m > last_measurement:
            increase += 1
        last_measurement = m
    print('part 1: ', increase)


def part2(data):
    increase = 0
    last_sum = None
    for i in range(len(data) - 2):
        current_sum = sum(data[i:i + 3])
        if last_sum and current_sum > last_sum:
            increase += 1
        last_sum = current_sum
    print('part 2: ', increase)


if __name__ == '__main__':
    input_data = []
    for line in open(INPUT_PATH, 'r', encoding='UTF-8'):
        input_data.append(int(line))

    part1(input_data)
    part2(input_data)


