# https://adventofcode.com/2021/day/3

INPUT_PATH = 'input.txt'


def part1(data):
    yv = abs(data[2]) - 1
    h = (yv * (yv + 1)) // 2
    print(h)


def part2(data):
    def is_valid(x, y):
        px, py = 0, 0
        while py > data[2]:
            px += x
            py += y
            x = x - 1 if x > 0 else 0
            y -= 1
            if data[2] <= py <= data[3] and data[0] <= px <= data[1]:
                return True
        return False

    options = 0
    minx = 0
    for x in range(data[0]):
        if (x * (x + 1)) // 2 >= data[0]:
            minx = x
            break
    rvx = (minx, data[1]+1)
    rvy = (data[2], abs(data[2])+1)

    for vx in range(*rvx):
        for vy in range(*rvy):
            if is_valid(vx, vy):
                options += 1
    print(options)


if __name__ == '__main__':
    # input_data = 20, 30, -10, -5
    input_data = 70, 125, -159, -121

    part1(input_data)
    part2(input_data)
