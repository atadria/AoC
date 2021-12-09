# https://adventofcode.com/2021/day/8
from collections import Counter

INPUT_PATH = 'input.txt'


def part1(data):
    cnt = 0
    lens = {2, 3, 4, 7}
    for _, x in data:
        for xx in x:
            if len(xx) in lens:
                cnt += 1
    print(cnt)


def part2(data):
    s0 = set('abcefg')
    s1 = set('cf')
    s2 = set('acdeg')
    s3 = set('acdfg')
    s4 = set('bcdf')
    s5 = set('abdfg')
    s6 = set('abdefg')
    s7 = set('acf')
    s8 = set('abcdefg')
    s9 = set('abcdfg')

    numbers = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]

    all_s = 'abcdefg'
    m_cnt = {}
    for s in all_s:
        m_cnt[s] = 0
        for n in numbers:
            if s in n:
                m_cnt[s] += 1
    # {'a': 8, 'b': 6, 'c': 8, 'd': 7, 'e': 4, 'f': 9, 'g': 7}

    cnt = 0
    for p1, p2 in data:
        map_s = {}
        cnt_s = Counter()
        for p in p1:
            cnt_s += Counter(p)
        v8ac = []
        v7dg = []
        for s, v in cnt_s.items():
            if v == 8:
                v8ac.append(s)
            elif v == 7:
                v7dg.append(s)
            elif v == 6:
                map_s[s] = 'b'
            elif v == 4:
                map_s[s] = 'e'
            elif v == 9:
                map_s[s] = 'f'
        # a is in 7 but not in 1
        # d is in 4, and g is not
        n1 = ''
        n4 = ''
        n7 = ''
        for n in p1:
            if len(n) == 2:
                n1 = n
            elif len(n) == 4:
                n4 = n
            elif len(n) == 3:
                n7 = n
        a = list(set(n7) - set(n1))[0]
        c = list(set(v8ac) - set(a))[0]
        g = list(set(v7dg) - set(n4))[0]
        d = list(set(v7dg) - set(g))[0]
        map_s[a] = 'a'
        map_s[c] = 'c'
        map_s[g] = 'g'
        map_s[d] = 'd'

        p2v = []
        for n in p2:
            nn = ''
            for x in n:
                nn += map_s[x]
            nn = set(nn)
            for i, num in enumerate(numbers):
                if nn == num:
                    p2v.append(i)
        cnt += int(''.join([str(x) for x in p2v]))
    print(cnt)


if __name__ == '__main__':
    input_data = []
    for line in open(INPUT_PATH, 'r', encoding='UTF-8'):
        p1, p2 = line.split('|')
        input_data.append((p1.strip().split(), p2.strip().split()))

    part1(input_data)
    part2(input_data)
