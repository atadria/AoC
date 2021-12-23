# https://adventofcode.com/2021/day/3

from collections import deque


INPUT_PATH = 'input.txt'

TEST = [4, 8]
INPUT = [6, 10]


def roll(n):
    result = 0
    for i in range(n + 1, n + 4):
        result += i % 100 if i % 100 != 0 else 100
    return result


def part1(data):
    p1 = 0
    p2 = 0
    pp1, pp2 = data
    cnt = 0
    while p1 < 1000 and p2 < 1000:
        pp1 += roll(cnt)
        cnt += 3
        pp1 = pp1 % 10 if pp1 % 10 != 0 else 10
        p1 += pp1
        if p1 < 1000:
            pp2 += roll(cnt)
            cnt += 3
            pp2 = pp2 % 10 if pp2 % 10 != 0 else 10
            p2 += pp2
        # print(p1, p2, cnt)
    print(cnt * min([p1, p2]))


def part2(data):
    c = [1, 2, 3]
    cc = {}
    for c1 in c:
        for c2 in c:
            for c3 in c:
                s = sum([c1, c2, c3])
                if s in cc:
                    cc[s] += 1
                else:
                    cc[s] = 1
    print(cc)

    p1w = 0
    p2w = 0
    pp = deque([(data[0], 0, data[1], 0, 1)])
    while pp:
        pp1, p1, pp2, p2, w = pp.pop()
        for k, v in cc.items():
            ppp1 = pp1 + k
            ppp1 = ppp1 % 10 if ppp1 % 10 != 0 else 10
            px1 = p1 + ppp1
            wx = w * v
            if px1 < 21:
                for kk, vv in cc.items():
                    ppp2 = pp2 + kk
                    ppp2 = ppp2 % 10 if ppp2 % 10 != 0 else 10
                    px2 = p2 + ppp2
                    wxx = wx * vv
                    if px2 < 21:
                        pp.append((ppp1, px1, ppp2, px2, wxx))
                    else:
                        p2w += wxx
            else:
                p1w += wx
    print(max(p1w, p2w))
    print(p1w, p2w)
    print(444356092776315, 341960390180808)


if __name__ == '__main__':
    input_data = INPUT

    part1(input_data)
    part2(input_data)
