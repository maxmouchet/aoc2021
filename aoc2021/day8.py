from collections import defaultdict

from aoc2021 import INPUTS


def decode(observations):
    observations_by_length = defaultdict(list)
    for observation in observations:
        observations_by_length[len(observation)].append(frozenset(observation))
    # Decode 1, 4, 7, 8
    digit_to_segments = {
        1: observations_by_length[2][0],
        4: observations_by_length[4][0],
        7: observations_by_length[3][0],
        8: observations_by_length[7][0],
    }
    # Decode 2, 3, 5
    for observation in observations_by_length[5]:
        if len(observation & digit_to_segments[1]) == 2:
            digit_to_segments[3] = observation
        elif len(observation & digit_to_segments[4]) == 3:
            digit_to_segments[5] = observation
        else:
            digit_to_segments[2] = observation
    # Decode 0, 6, 9
    for observation in observations_by_length[6]:
        if observation == digit_to_segments[3] | digit_to_segments[4]:
            digit_to_segments[9] = observation
        elif len(observation & digit_to_segments[1]) == 2:
            digit_to_segments[0] = observation
        else:
            digit_to_segments[6] = observation
    return {segments: digit for digit, segments in digit_to_segments.items()}


def main():
    total_1, total_2 = 0, 0
    with (INPUTS / "day8.txt").open() as f:
        for line in f:
            left, right = line.split("|")
            segments_to_digit = decode(left.split())
            for i, segments in enumerate(right.split()):
                digit = segments_to_digit[frozenset(segments)]
                if digit in {1, 4, 7, 8}:
                    total_1 += 1
                total_2 += 10 ** (3 - i) * digit
    print(total_1, total_2)


if __name__ == "__main__":
    main()
