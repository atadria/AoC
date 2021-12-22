# https://adventofcode.com/2021/day/3

# INPUT_PATH = 'test.txt'
INPUT_PATH = 'input.txt'

DX = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
DY = [-1, -1, -1, 0, 0, 0, 1, 1, 1]


def part1(data, pattern):
    default = '0'
    for n in range(2):
        ly = len(data)
        lx = len(data[0])
        new_data = []
        l = 0
        for i in range(-2, ly+2):
            new_row = ''
            for j in range(-2, lx+2):
                number = ''
                for dx, dy in zip(DX, DY):
                    if 0 <= j + dx < lx and 0 <= i + dy < ly:
                        number += '1' if data[i + dy][j + dx] == '#' else '0'
                    else:
                        number += default
                number = int(number, 2)
                ch = pattern[number]
                new_row += ch
                if ch == '#':
                    l += 1
            new_data.append(new_row)
        default = '0' if default == '1' else '1'
        data = new_data
        for row in data:
            print(row)
    print(l)



def part2(data, pattern):
    default = '0'
    for n in range(50):
        ly = len(data)
        lx = len(data[0])
        new_data = []
        l = 0
        for i in range(-2, ly + 2):
            new_row = ''
            for j in range(-2, lx + 2):
                number = ''
                for dx, dy in zip(DX, DY):
                    if 0 <= j + dx < lx and 0 <= i + dy < ly:
                        number += '1' if data[i + dy][j + dx] == '#' else '0'
                    else:
                        number += default
                number = int(number, 2)
                ch = pattern[number]
                new_row += ch
                if ch == '#':
                    l += 1
            new_data.append(new_row)
        default = '0' if default == '1' else '1'
        data = new_data
    print(l)


if __name__ == '__main__':
    input_data = []
    for i, line in enumerate(open(INPUT_PATH, 'r')):
        if i > 1:
            input_data.append(line.strip())
        elif i == 0:
            pattern = line.strip()

    part1(input_data, pattern)
    part2(input_data, pattern)
