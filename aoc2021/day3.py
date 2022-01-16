from collections import defaultdict

from aoc2021 import INPUTS


def most_common_bits(values):
    """
    >>> values = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    >>> most_common_bits(values)
    '10110'
    """
    total = 0
    zeros = defaultdict(int)
    for value in values:
        total += 1
        for i, bit in enumerate(value.strip()):
            zeros[i] += bit == "0"
    result = ["0"] * len(zeros)
    for i, count in zeros.items():
        if count > total / 2:
            result[i] = "0"
        else:
            result[i] = "1"
    return "".join(result)


def decode_rate(values):
    """
    >>> values = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    >>> decode_rate(values)
    (22, 9)
    """
    most_common = most_common_bits(values)
    gamma = int(most_common, base=2)
    epsilon = gamma ^ (2 ** len(most_common) - 1)
    return gamma, epsilon


def decode_rating(values):
    """
    >>> values = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    >>> decode_rating(values)
    (23, 10)
    """
    # Is there a streaming solution for this problem?
    oxygen_values = list(values)
    co2_values = oxygen_values.copy()
    for i in range(len(oxygen_values[0].strip())):
        most_common = most_common_bits(oxygen_values)
        oxygen_values = [x for x in oxygen_values if x[i] == most_common[i]]
        if len(oxygen_values) == 1:
            break
    for i in range(len(co2_values[0].strip())):
        most_common = most_common_bits(co2_values)
        co2_values = [x for x in co2_values if x[i] != most_common[i]]
        if len(co2_values) == 1:
            break
    oxygen = int(oxygen_values[0], base=2)
    co2 = int(co2_values[0], base=2)
    return oxygen, co2


def main():
    with (INPUTS / "day3.txt").open() as f:
        gamma, epsilon = decode_rate(f)
        print(gamma * epsilon)
        f.seek(0)
        oxygen, co2 = decode_rating(f)
        print(oxygen * co2)


if __name__ == "__main__":
    main()
