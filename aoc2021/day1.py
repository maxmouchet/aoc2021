from collections import deque


def count_increases(values, *, window):
    """
    >>> values = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    >>> count_increases(values, window=1)
    7
    >>> count_increases(values, window=3)
    5
    """
    ring = deque([], maxlen=window)
    increases = 0
    for value in values:
        previous = sum(ring)
        ring.append(value)
        if len(ring) >= window:
            current = sum(ring)
            if current > previous:
                increases += 1
    return increases - 1


def main():
    with open("inputs/day1.txt") as f:
        print(count_increases((int(line) for line in f), window=1))
        f.seek(0)
        print(count_increases((int(line) for line in f), window=3))


if __name__ == "__main__":
    main()
