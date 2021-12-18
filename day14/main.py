# https://adventofcode.com/2021/day/14
from collections import Counter

# INPUT_PATH = 'test.txt'
INPUT_PATH = 'input.txt'


def part1(data, start):
    s = start[:]
    for n in range(10):
        new_str = ''
        for a, b in zip(s[:-1], s[1:]):
            ab = ''.join([a, b])
            new_str = new_str[:-1] + ''.join([a, data[ab], b])
        s = new_str[:]
        print(n)
    cnt = Counter(s)
    cntmc = cnt.most_common()
    mc = cntmc[0][1]
    lc = cntmc[-1][1]
    print(mc - lc)


def part2(data, start):
    s = start[:]
    pcnt = {}
    for a, b in zip(s[:-1], s[1:]):
        ab = ''.join([a, b])
        if ab in pcnt:
            pcnt[ab] += 1
        else:
            pcnt[ab] = 1
    for n in range(40):
        npcnt = {}
        for ab, v in pcnt.items():
            a, b = ab
            ac = a + data[ab]
            cb = data[ab] + b
            for p in [ac, cb]:
                if p in npcnt:
                    npcnt[p] += v
                else:
                    npcnt[p] = v
        pcnt = npcnt
    cnt = Counter()
    for k, v in pcnt.items():
        for x in k:
            cnt[x] += v
    cntmc = cnt.most_common()
    mc = cntmc[0][1]
    if mc in [start[0], start[-1]]:
        mc += 1
    lc = cntmc[-1][1]
    if lc in [start[0], start[-1]]:
        lc += 1
    # we count elements in pairs twice - except first and last
    print((mc - lc)//2)


if __name__ == '__main__':
    input_data = {}
    start = ''
    for i, line in enumerate(open(INPUT_PATH, 'r', encoding='UTF-8')):
        if i >= 2:
            a, _, b = line.strip().split()
            input_data[a] = b
        elif line.strip():
            start = line.strip()

    part1(input_data, start)
    part2(input_data, start)
