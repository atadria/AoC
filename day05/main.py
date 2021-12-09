# https://adventofcode.com/2021/day/5

INPUT_PATH = 'input.txt'


def part1(data, tab):
    tab = tab[:]
    for p1, p2 in data:
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            if y1 < y2:
                for yi in range(y1, y2+1):
                    tab[yi][x1] += 1
            else:
                for yi in range(y2, y1+1):
                    tab[yi][x1] += 1
        elif y1 == y2:
            if x1 < x2:
                for xi in range(x1, x2+1):
                    tab[y1][xi] += 1
            else:
                for xi in range(x2, x1+1):
                    tab[y1][xi] += 1
    result = 0
    for row in tab:
        for el in row:
            if el > 1:
                result += 1
    print result


def part2(data, tab):
    tab = tab[:]
    for p1, p2 in data:
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            if y1 < y2:
                for yi in range(y1, y2 + 1):
                    tab[yi][x1] += 1
            else:
                for yi in range(y2, y1 + 1):
                    tab[yi][x1] += 1
        elif y1 == y2:
            if x1 < x2:
                for xi in range(x1, x2 + 1):
                    tab[y1][xi] += 1
            else:
                for xi in range(x2, x1 + 1):
                    tab[y1][xi] += 1
        else:
            if x1 < x2 and y1 < y2:
                x = range(x1, x2+1)
                y = range(y1, y2+1)
            elif x1 < x2 and y1 > y2:
                x = range(x1, x2+1)
                y = range(y1, y2-1, -1)
            elif x1 > x2 and y1 < y2:
                x = range(x1, x2-1, -1)
                y = range(y1, y2+1)
            else:
                x = range(x1, x2 - 1, -1)
                y = range(y1, y2-1, -1)
            for xi, yi in zip(x, y):
                tab[yi][xi] += 1
    result = 0
    for row in tab:
        for el in row:
            if el > 1:
                result += 1
    print result


if __name__ == '__main__':
    input_data = []
    for line in open(INPUT_PATH, 'r'):
        p1, _, p2 = line.strip().split()
        input_data.append(([int(x) for x in p1.split(',')], [int(x) for x in p2.split(',')]))
    xmax, ymax = 0, 0
    for p1, p2 in input_data:
        x1, y1 = p1
        x2, y2 = p2
        xmax = max([x1, x2, xmax])
        ymax = max([y1, y2, ymax])

    table = []
    for r in range(ymax+1):
        table.append([0] * (xmax + 1))
    part1(input_data, table)
    part2(input_data, table)
