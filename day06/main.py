# https://adventofcode.com/2021/day/3

from collections import Counter

INPUT_PATH = 'input.txt'


def part1(data):
    cnt = Counter(data)
    for i in range(80):
        tmp_cnt = Counter()
        new = 0
        for x in cnt:
            if x == 0:
                new += cnt[x]
                tmp_cnt[8] = cnt[x]
            else:
                tmp_cnt[x-1] = cnt[x]
        tmp_cnt[6] += new
        cnt = tmp_cnt
    print(sum(cnt.values()))


def part2(data):
    cnt = Counter(data)
    for i in range(256):
        tmp_cnt = Counter()
        new = 0
        for x in cnt:
            if x == 0:
                new += cnt[x]
                tmp_cnt[8] = cnt[x]
            else:
                tmp_cnt[x - 1] = cnt[x]
        tmp_cnt[6] += new
        cnt = tmp_cnt
    print(sum(cnt.values()))


if __name__ == '__main__':
    for line in open(INPUT_PATH, 'r', encoding='UTF-8'):
        input_data = [int(x) for x in line.split(',')]

    part1(input_data)
    part2(input_data)
