# https://adventofcode.com/2021/day/3

INPUT_PATH = 'input.txt'


def part1(numbers, cards):
    winning_bords = []
    results = []
    for num in numbers:
        for card_nbr, card in enumerate(cards):
            for row_nbr, row in enumerate(card):
                if num in row:
                    for i, n in enumerate(row):
                        if n == num:
                            cards[card_nbr][row_nbr][i] = -1
                            # check row
                            if sum(row) == -5:
                                score = 0
                                for x in cards[card_nbr]:
                                    score += sum(x)

                                print('row', card_nbr + 1, score * num)
                                if card_nbr not in winning_bords:
                                    winning_bords.append(card_nbr)
                                    results.append(score * num)
                            # check column
                            else:
                                col_sum = 0
                                for rowx in cards[card_nbr]:
                                    col_sum += rowx[i]
                                if col_sum == -5:
                                    score = 0
                                    for x in cards[card_nbr]:
                                        score += sum(x)
                                    print(card_nbr + 1, score * num, num)
                                    if card_nbr not in winning_bords:
                                        winning_bords.append(card_nbr)
                                        results.append(score * num)
    print(results[-1])


def part2(numbers, cards):
    pass


if __name__ == '__main__':
    input_data = []
    for line in open(INPUT_PATH, 'r', encoding='UTF-8'):
        input_data.append(line.strip())

    numbers = [int(x) for x in input_data[0].split(',')]

    cards = []
    current = []
    for line in input_data[2:]:
        if line:
            current.append([int(x) for x in line.split()])
        else:
            cards.append(current)
            current = []

    part1(numbers, cards)
    part2(numbers, cards)
