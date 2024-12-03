import re


def part_1(data):
    return sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", data))


def part_2(data):
    result = 0
    ignore = False
    for instruction in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", data):
        if instruction.group(0) == "do()":
            ignore = False
        elif instruction.group(0) == "don't()":
            ignore = True
        elif not ignore:
            result += int(instruction.group(1)) * int(instruction.group(2))
    return result


if __name__ == "__main__":
    with open("day_03_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
