# https://adventofcode.com/2021/day/3
from collections import deque

INPUT_PATH = 'input.txt'
# INPUT_PATH = 'test.txt'

gi = [0, 0, 1, 1, 1, -1, -1, -1]
gj = [1, -1, 1, -1, 0, 1, -1, 0]


def part1(data):
    flashes = 0
    mi = len(data)
    mj = len(data[0])
    for n in range(100):
        q = deque()
        f = []
        data = [[y+1 for y in x] for x in data]

        for i in range(mi):
            for j in range(mj):
                if data[i][j] > 9:
                    q.append((i, j))
                    f.append((i, j))
        while q:
            i, j = q.pop()
            for di, dj in zip(gi, gj):
                if 0 <= i + di < mi and 0 <= j + dj < mj:
                    data[i + di][j + dj] += 1
                    if data[i + di][j + dj] > 9 and (i + di, j + dj) not in f:
                        f.append((i + di, j + dj))
                        q.append((i + di, j + dj))
        for i in range(mi):
            for j in range(mj):
                if data[i][j] > 9:
                    data[i][j] = 0
        flashes += len(f)
    print(flashes)


def part2(data):
    mi = len(data)
    mj = len(data[0])
    for n in range(1000):
        q = deque()
        f = []
        data = [[y + 1 for y in x] for x in data]

        for i in range(mi):
            for j in range(mj):
                if data[i][j] > 9:
                    q.append((i, j))
                    f.append((i, j))
        while q:
            i, j = q.pop()
            for di, dj in zip(gi, gj):
                if 0 <= i + di < mi and 0 <= j + dj < mj:
                    data[i + di][j + dj] += 1
                    if data[i + di][j + dj] > 9 and (i + di, j + dj) not in f:
                        f.append((i + di, j + dj))
                        q.append((i + di, j + dj))
        for i in range(mi):
            for j in range(mj):
                if data[i][j] > 9:
                    data[i][j] = 0
        if len(f) == mi*mj:
            print(n+1)
            break


if __name__ == '__main__':
    input_data = []
    for line in open(INPUT_PATH, 'r'):
        input_data.append([int(x) for x in line.strip()])

    part1(input_data)
    part2(input_data)
