import math

from aoc2021 import INPUTS


def evaluate(positions, target, *, weighted):
    """
    >>> positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    >>> evaluate(positions, 1, weighted=False)
    41
    >>> evaluate(positions, 2, weighted=False)
    37
    >>> evaluate(positions, 10, weighted=False)
    71
    >>> evaluate(positions, 5, weighted=True)
    168
    """
    f = lambda x: x
    if weighted:
        f = lambda x: x * (x + 1) // 2
    return sum(f(abs(position - target)) for position in positions)


def minimize(positions, *, weighted):
    best = math.inf
    for i in range(min(positions), max(positions)):
        candidate = evaluate(positions, i, weighted=weighted)
        if candidate > best:
            return best
        best = candidate


def main():
    with (INPUTS / "day7.txt").open() as f:
        positions = [int(x) for x in next(f).split(",")]
    print(minimize(positions, weighted=False))
    print(minimize(positions, weighted=True))


if __name__ == "__main__":
    main()
