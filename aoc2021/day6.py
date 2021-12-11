from collections import defaultdict


def step(timers):
    """
    >>> step([3, 4, 3, 1, 2])
    [2, 3, 2, 0, 1]
    >>> step([2, 3, 2, 0, 1])
    [1, 2, 1, 6, 0, 8]
    """
    new = []
    children = 0
    for timer in timers:
        if timer == 0:
            new.append(6)
            children += 1
        else:
            new.append(timer - 1)
    return new + [8] * children


def simulate(timers, *, days):
    """
    >>> simulate([3,4,3,1,2], days=18)
    [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8]
    >>> len(simulate([3,4,3,1,2], days=18))
    26
    >>> len(simulate([3,4,3,1,2], days=80))
    5934
    """
    for day in range(days):
        timers = step(timers)
    return timers


def main():
    with open("inputs/day6.txt") as f:
        timers = [int(x) for x in next(f).split(",")]
    print(len(simulate(timers, days=80)))
    lengths = defaultdict(int)
    for timer in timers:
        if timer not in lengths:
            lengths[timer] = len(simulate([timer], days=256))
            print(lengths)
    print(sum(lengths[timer] for timer in timers))


if __name__ == "__main__":
    main()
