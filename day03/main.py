# https://adventofcode.com/2021/day/3

import numpy as np


INPUT_PATH = 'input.txt'


def part1(data):
    d = data.sum(axis=0)/data.shape[0]
    a = ''.join([str(x) for x in (d >= 0.5).astype(int)])
    b = ''.join([str(x) for x in (d < 0.5).astype(int)])
    print(int(a, 2) * int(b, 2))


def part2(data):
    data_len = data.shape[1]
    most_common = data
    least_common = data
    for i in range(data_len):
        md = most_common.sum(axis=0)/most_common.shape[0]
        most_common_bits = (md >= 0.5).astype(int)
        most_common = most_common[most_common[:, i] == most_common_bits[i]]
        if least_common.shape[0] > 1:
            ld = least_common.sum(axis=0) / least_common.shape[0]
            least_common_bits = (ld < 0.5).astype(int)
            least_common = least_common[least_common[:, i] == least_common_bits[i]]
    a = ''.join([str(x) for x in most_common[0]])
    b = ''.join([str(x) for x in least_common[0]])
    print(int(a, 2) * int(b, 2))


if __name__ == '__main__':
    input_data = []
    for line in open(INPUT_PATH, 'r', encoding='UTF-8'):
        input_data.append([int(x) for x in line.strip()])

    input_data = np.array(input_data)

    part1(input_data)
    part2(input_data)
