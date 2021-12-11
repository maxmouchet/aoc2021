import math

BOARD_1 = [
    [22, 13, 17, 11, 0],
    [8, 2, 23, 4, 24],
    [21, 9, 14, 16, 7],
    [6, 10, 3, 18, 5],
    [1, 12, 20, 15, 19],
]

BOARD_2 = [
    [3, 15, 0, 2, 22],
    [9, 18, 13, 17, 5],
    [19, 8, 7, 25, 23],
    [20, 11, 10, 24, 4],
    [14, 21, 16, 12, 6],
]

BOARD_3 = [
    [14, 21, 17, 24, 4],
    [10, 16, 15, 9, 19],
    [18, 8, 23, 26, 20],
    [22, 11, 13, 6, 5],
    [2, 0, 12, 3, 7],
]

# fmt: off
NUMBERS = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
# fmt: on


def play(board, numbers):
    """
    >>> play(BOARD_3, NUMBERS)
    (11, 24, 188)
    """
    nrows, ncols = len(board), len(board[0])
    rowscore = [0] * nrows
    colscore = [0] * ncols
    position = {}
    total = 0
    for i in range(nrows):
        for j in range(ncols):
            position[board[i][j]] = (i, j)
            total += board[i][j]
    for n, number in enumerate(numbers):
        if pos := position.get(number):
            total -= number
            i, j = pos
            rowscore[i] += 1
            colscore[j] += 1
            if rowscore[i] == nrows:
                return n, number, total
            if colscore[j] == ncols:
                return n, number, total
    return None


def find_winning_board(boards, numbers):
    """
    >>> find_winning_board([BOARD_1, BOARD_2, BOARD_3], NUMBERS)
    (11, 24, 188)
    """
    best = (math.inf, math.inf, math.inf)
    for board in boards:
        if result := play(board, numbers):
            best = min(best, result)
    return best


def find_loosing_board(boards, numbers):
    """
    >>> find_loosing_board([BOARD_1, BOARD_2, BOARD_3], NUMBERS)
    (14, 13, 148)
    """
    best = (0, 0, 0)
    for board in boards:
        if result := play(board, numbers):
            best = max(best, result)
    return best


def main():
    with open("inputs/day4.txt") as f:
        numbers = [int(x) for x in next(f).split(",")]
        boards = []
        for line in f:
            line = line.strip()
            if line:
                boards[-1].append([int(x) for x in line.split()])
            else:
                boards.append([])
        n, number, total = find_winning_board(boards, numbers)
        print(number * total)
        n, number, total = find_loosing_board(boards, numbers)
        print(number * total)


if __name__ == "__main__":
    main()
