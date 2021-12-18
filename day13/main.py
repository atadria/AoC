# https://adventofcode.com/2021/day/3

INPUT_PATH = 'input.txt'


def part1(data, folds, maxx, maxy):
    m = [['.' for x in range(maxx+1)] for y in range(maxy+1)]
    for x, y in data:
        m[y][x] = '#'
    f, fv = folds[0]
    fv = int(fv)
    if f == 'y':
        m1 = m[:fv]
        m2 = m[fv+1:][::-1]
    if f == 'x':
        m1 = [x[:fv] for x in m]
        m2 = [x[fv+1:][::-1] for x in m]

    cnt = 0
    new = [['.' for x in range(maxx)] for y in range(len(m1))]
    for i, (r1, r2) in enumerate(zip(m1, m2)):
        for j, (e1, e2) in enumerate(zip(r1, r2)):
            if '#' in (e1, e2):
                cnt += 1
                new[i][j] = '#'
    print(cnt)


def part2(data, folds, maxx, maxy):
    m = [['.' for x in range(maxx + 1)] for y in range(maxy + 1)]
    for x, y in data:
        m[y][x] = '#'
    for f, fv in folds:
        fv = int(fv)
        if f == 'y':
            m1 = m[:fv]
            m2 = m[fv + 1:]
            m2.reverse()
            if len(m1) > len(m2):
                m2 = [['.' for x in range(len(m1[0]))] for y in range(len(m1) - len(m2))] + m2
            elif len(m1) < len(m2):
                m1 = [['.' for x in range(len(m1[0]))] for y in range(len(m2) - len(m1))] + m1
        if f == 'x':
            m1l = fv
            m2l = len(m[0]) - (fv + 1)
            m1 = [x[:fv] for x in m]
            m2 = [x[fv + 1:][::-1] for x in m]
            if m1l > m2l:
                m2 = [[['.'] * (m1l - m2l) + x for x in m2]]
            elif len(m1) < len(m2):
                m1 = [[['.'] * (m2l - m1l) + x for x in m1]]
        new = [['.' for x in range(len(m1[0]))] for y in range(len(m1))]
        for i, (r1, r2) in enumerate(zip(m1, m2)):
            for j, (e1, e2) in enumerate(zip(r1, r2)):
                if '#' in (e1, e2):
                    new[i][j] = '#'
        m = new
    cnt = 0
    for r in m:
        print(r)
        for e in r:
            if e == '#':
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    input_data = []
    folds = []
    maxx = 0
    maxy = 0
    for line in open(INPUT_PATH, 'r', encoding='UTF-8'):
        if line[0].isnumeric():
            a, b = [int(x) for x in line.strip().split(',')]
            input_data.append([a, b])
            if a > maxx:
                maxx = a
            if b > maxy:
                maxy = b
        elif line.strip():
            folds.append(line.strip().split()[-1].split('='))

    part1(input_data, folds, maxx, maxy)
    part2(input_data, folds, maxx, maxy)
