from functools import reduce
import operator


def solution() -> str:
    with open('data/input_2.txt', 'r') as input_data:
        presents = [[int(y) for y in x.strip().split('x')] for x in input_data.read().split('\n')]

    return f'Part 1: {part_1(presents)} / Part 2: {part_2(presents)}'


def part_1(presents: list[list[int]]) -> str:
    sqr_feet = 0
    for present in presents:
        amount = (2 * present[0] * present[1]) + (2 * present[1] * present[2]) + (2 * present[2] * present[0])
        slack = (present[0] * present[1] * present[2]) // max(present)
        sqr_feet += amount + slack

    return str(sqr_feet)


def part_2(presents: list[list[int]]) -> str:
    sqr_feet = 0
    for present in presents:
        amount = 2 * sum(present) - 2 * max(present)
        bow = reduce(operator.mul, present, 1)
        sqr_feet += amount + bow

    return str(sqr_feet)
