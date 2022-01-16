from aoc2021 import INPUTS


def simulate(timers, *, days):
    """
    >>> sum(simulate([3,4,3,1,2], days=18))
    26
    >>> sum(simulate([3,4,3,1,2], days=80))
    5934
    """
    state = [0] * 9
    for timer in timers:
        state[timer] += 1
    for day in range(days):
        expired = state[0]
        state = state[1:] + [0]
        state[6] += expired
        state[8] += expired
    return state


def main():
    with (INPUTS / "day6.txt").open() as f:
        timers = [int(x) for x in next(f).split(",")]
    print(sum(simulate(timers, days=80)))
    print(sum(simulate(timers, days=256)))


if __name__ == "__main__":
    main()
