# https://adventofcode.com/2021/day/3
from collections import defaultdict, deque

INPUT_PATH = 'input.txt'
# INPUT_PATH = 'test.txt'


def part1(data):
    points = {')': 3,
              ']': 57,
              '}': 1197,
              '>': 25137}

    oc = {'(': ')',
          '[': ']',
          '{': '}',
          '<': '>'}

    error_cnt = defaultdict(int)
    for l in data:
        stack = deque()
        for ch in l:
            if ch in oc:
                stack.append(ch)
            else:
                if stack:
                    last = stack.pop()
                    if ch != oc[last]:
                        error_cnt[ch] += 1
                else:
                    error_cnt[ch] += 1
    print(error_cnt)
    print(sum([v * points[k] for k, v in error_cnt.items()]))


def part2(data):
    points = {'(': 1,
              '[': 2,
              '{': 3,
              '<': 4}

    oc = {'(': ')',
          '[': ']',
          '{': '}',
          '<': '>'}

    stacks = []
    for l in data:
        stack = deque()
        is_corrupted = False
        for ch in l:
            if ch in oc:
                stack.append(ch)
            else:
                if stack:
                    last = stack.pop()
                    if ch != oc[last]:
                        is_corrupted = True
                        break
                else:
                    is_corrupted = True
                    break
        if not is_corrupted:
            stacks.append(stack)

    p = []
    for s in stacks:
        pp = 0
        while s:
            pp = (pp*5) + points[s.pop()]
        p.append(pp)
    p.sort()
    print(p[len(p)/2])


if __name__ == '__main__':
    input_data = []
    for line in open(INPUT_PATH, 'r'):
        input_data.append(line.strip())

    part1(input_data)
    part2(input_data)
