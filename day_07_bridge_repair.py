import itertools
import operator


def part_1(data):
    output = 0
    for line in data:
        result, *values = map(int, line.replace(":", "").split())
        if solve(values, [operator.add, operator.mul], result):
            output += result
    return output


def part_2(data):
    def concatenate(a, b):
        return int(str(a) + str(b))

    output = 0
    for line in data:
        result, *values = map(int, line.replace(":", "").split())
        if solve(values, [operator.add, operator.mul, concatenate], result):
            output += result
    return output


def solve(values, operators, result):
    if values[0] > result:
        return False
    if len(values) == 1:
        return result == values[0]
    return any(solve([op(*values[:2]), *values[2:]], operators, result) for op in operators)


if __name__ == "__main__":
    with open("day_07_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
