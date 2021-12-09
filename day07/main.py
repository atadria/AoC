# https://adventofcode.com/2021/day/3

INPUT_PATH = 'input.txt'
# INPUT_PATH = 'test.txt'


def part1(data):
    costs = {}
    for p in range(max(data)):
        costs[p] = 0
        for x in data:
            costs[p] += abs(p - x)
    print(min(costs.values()))


def part2(data):
    costs = {}
    change_cost = {}
    for p in range(max(data)):
        costs[p] = 0
        for x in data:
            if p != x:
                change = abs(p - x)
                if change in change_cost:
                    cc = change_cost[change]
                else:
                    cc = sum(list(range(1, abs(p - x) + 1)))
                    change_cost[change] = cc
                costs[p] += cc
    print(min(costs.values()))


if __name__ == '__main__':
    for line in open(INPUT_PATH, 'r', encoding='UTF-8'):
        input_data = [int(x) for x in line.split(',')]

    part1(input_data)
    part2(input_data)
