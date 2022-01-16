from collections import defaultdict

from aoc2021 import INPUTS


def count_intersections(lines, *, with_diagonals):
    """
    >>> lines = [(0,9,5,9), (8,0,0,8), (9,4,3,4), (2,2,2,1), (7,0,7,4), (6,4,2,0), (0,9,2,9), (3,4,1,4), (0,0,8,8), (5,5,8,2)]
    >>> count_intersections(lines, with_diagonals=False)
    5
    >>> count_intersections(lines, with_diagonals=True)
    12
    """
    grid = defaultdict(int)
    for x1, y1, x2, y2 in lines:
        if not with_diagonals and x1 != x2 and y1 != y2:
            continue
        grid[(x1, y1)] += 1
        while x1 != x2 or y1 != y2:
            if x1 < x2:
                x1 += 1
            if x1 > x2:
                x1 -= 1
            if y1 < y2:
                y1 += 1
            if y1 > y2:
                y1 -= 1
            grid[(x1, y1)] += 1
    return sum(x > 1 for x in grid.values())


def main():
    with (INPUTS / "day5.txt").open() as f:
        lines = []
        for line in f:
            lines.append(
                [int(x) for x in line.replace(",", " ").replace("->", " ").split()]
            )
        print(count_intersections(lines, with_diagonals=False))
        print(count_intersections(lines, with_diagonals=True))


if __name__ == "__main__":
    main()
