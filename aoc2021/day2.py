from aoc2021 import INPUTS


def compute_position(commands, *, with_aim):
    """
    >>> commands = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    >>> compute_position(commands, with_aim=False)
    (15, 10)
    >>> compute_position(commands, with_aim=True)
    (15, 60)
    """
    horizontal, depth, aim = 0, 0, 0
    for command in commands:
        match command.split():
            case "forward", n:
                horizontal += int(n)
                depth += aim * int(n) * with_aim
            case "down", n:
                aim += int(n)
                depth += int(n) * (not with_aim)
            case "up", n:
                aim -= int(n)
                depth -= int(n) * (not with_aim)
    return horizontal, depth


def main():
    with (INPUTS / "day2.txt").open() as f:
        horizontal, depth = compute_position(f, with_aim=False)
        print(horizontal * depth)
        f.seek(0)
        horizontal, depth = compute_position(f, with_aim=True)
        print(horizontal * depth)


if __name__ == "__main__":
    main()
