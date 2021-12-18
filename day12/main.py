# https://adventofcode.com/2021/day/3

from collections import deque, Counter

INPUT_PATH = 'input.txt'
# INPUT_PATH = 'test.txt'

S = 'start'
E = 'end'

def part1(data):

    def is_valid(cave, current_path):
        c1 = cave != S
        c2 = cave.isupper()
        c3 = cave.islower() and cave not in current_path
        return c1 and (c2 or c3)

    paths = []
    to_explore = deque([[S, d] for d in data[S]])

    while to_explore:
        path = to_explore.pop()
        if path:
            last = path[-1]
            if last == E:
                p = ''.join(path)
                if p not in paths:
                    paths.append(p)
            else:
                for c in data[last]:
                    np = [x for x in path]
                    if is_valid(c, np):
                        np.append(c)
                        if np not in to_explore:
                            to_explore.append(np)
    print(len(paths))


def part2(data):
    def is_valid(cave, current_path):
        c1 = cave != S
        c2 = cave.isupper()
        c3 = cave.islower() and cave not in current_path
        cnt = Counter([xx for xx in current_path if xx.islower()])
        c4 = cave != E and cnt.most_common(1)[0][1] == 1
        return c1 and (c2 or c3 or c4)

    paths = []
    to_explore = deque([[S, d] for d in data[S]])

    while to_explore:
        path = to_explore.pop()
        if path:
            last = path[-1]
            if last == E:
                p = ''.join(path)
                if p not in paths:
                    paths.append(p)
            else:
                for c in data[last]:
                    np = [x for x in path]
                    if is_valid(c, np):
                        np.append(c)
                        if np not in to_explore:
                            to_explore.append(np)
    print(len(paths))


if __name__ == '__main__':

    m = {}
    for line in open(INPUT_PATH, 'r'):
        a, b = line.strip().split('-')
        if a not in m:
            m[a] = [b]
        else:
            m[a].append(b)
        if b not in m:
            m[b] = [a]
        else:
            m[b].append(a)

    print(m)

    part1(m)
    part2(m)
