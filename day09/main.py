# https://adventofcode.com/2021/day/3

# INPUT_PATH = 'test.txt'
INPUT_PATH = 'input.txt'


def part1(data):
    mins = []
    ii = len(data)
    jj = len(data[0])
    for i in range(ii):
        for j in range(jj):
            x = data[i][j]
            nn = []
            if i > 0:
                nn.append(data[i-1][j])
            if i + 1 < ii:
                nn.append(data[i+1][j])
            if j > 0:
                nn.append(data[i][j-1])
            if j + 1 < jj:
                nn.append(data[i][j+1])
            is_min = True
            for n in nn:
                if n <= x:
                    is_min = False
            if is_min:
                mins.append(x+1)
    print(mins)
    print(sum(mins))


def part2(data):
    def change_nn(ci, cj, cnt):
        ch = []
        if 0 <= data[ci][cj] < 9:
            data[ci][cj] = -1
        if ci > 0 and 0 <= data[ci-1][cj] < 9:
            data[ci - 1][cj] = -1
            ch.append((ci-1, cj))
        if ci + 1 < ii and 0 <= data[ci+1][cj] < 9:
            data[ci + 1][cj] = -1
            ch.append((ci + 1, cj))
        if cj > 0 and 0 <= data[ci][cj-1] < 9:
            data[ci][cj-1] = -1
            ch.append((ci, cj-1))
        if cj + 1 < jj and 0 <= data[ci][cj+1] < 9:
            data[ci][cj + 1] = -1
            ch.append((ci, cj+1))
        cnt.append(len(ch))
        for c in ch:
            change_nn(c[0], c[1], cnt)
        return cnt
    bb = []
    ii = len(data)
    jj = len(data[0])
    for i in range(ii):
        for j in range(jj):
            b = 0
            if 0 <= data[i][j] < 9:
                cntx = [1]
                change_nn(i, j, cntx)
                bb.append(sum(cntx))
    bb.sort()
    print(bb[-1]*bb[-2]*bb[-3])


if __name__ == '__main__':
    input_data = []
    for line in open(INPUT_PATH, 'r', encoding='UTF-8'):
        input_data.append([int(x) for x in line.strip()])

    part1(input_data)
    part2(input_data)
