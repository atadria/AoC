# https://adventofcode.com/2021/day/3

from collections import deque

# INPUT_PATH = 'test.txt'
INPUT_PATH = 'input.txt'

DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]
# DX = [1, 0]
# DY = [0, 1]


def part1(data):
    min_risk = (len(data[0]) + len(data)) * 5
    end = (len(data)-1, len(data[0])-1)
    maxx, maxy = end
    pos, cost = (0, 0), 0
    q = deque([(pos, cost)])
    pr = {(0, 0): 0, end: min_risk}
    while q:
        p, c = q.popleft()
        if p == end and c < min_risk:
            print(c)
            min_risk = c
            pr[end] = c
        else:
            for dx, dy in zip(DX, DY):
                x, y = p
                nx, ny = x+dx, y+dy
                if 0 <= nx <= maxx and 0 <= ny <= maxy:
                    nc = c + data[ny][nx]
                    if nc < min_risk:
                        if (nx, ny) not in pr or nc < pr[(nx, ny)]:
                            q.append(((nx, ny), nc))
                            pr[(nx, ny)] = nc
    print(min_risk)


def part2(data):
    mdata = []
    end = (len(data) - 1, len(data[0]) - 1)
    maxx, maxy = end
    for i in range(len(data)*5):
        row = []
        for j in range(len(data[0])*5):
            ii = i%(maxx+1)
            jj = j%(maxy+1)
            di = i//(maxx+1)
            dj = j//(maxy+1)
            v = data[ii][jj] + di +dj
            v = v if v <= 9 else v%9
            row.append(v)
        # print(''.join([str(x) for x in row]))
        mdata.append(row)
    part1(mdata)


if __name__ == '__main__':
    input_data = []
    for line in open(INPUT_PATH, 'r', encoding='UTF-8'):
        input_data.append([int(x) for x in line.strip()])

    # part1(input_data)
    part2(input_data)
