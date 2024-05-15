def solution() -> str:
    with open('data/input_1.txt', 'r') as input_data:
        input_string = input_data.read()
    return f'Part 1: {part_1(input_string)} / Part 2: {part_2(input_string)}'


def part_1(input_string: str) -> str:
    count = 0

    for par in input_string:
        if par == '(':
            count += 1
        else:
            count -= 1

    return str(count)


def part_2(input_string: str) -> str:
    count = 0

    for idx in range(len(input_string)):
        current = input_string[idx]
        if current == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return str(idx+1)
