import itertools


def part_1(data):
    return sum(safe([int(i) for i in line.split()]) for line in data)


def part_2(data):
    reports = [[int(i) for i in line.split()] for line in data]
    return sum(any(safe(c) for c in itertools.combinations(levels, r=len(levels)-1))
               for levels in reports)


def safe(levels):
    return (all(1 <= a - b <= 3 for a, b in zip(levels, levels[1:])) or
            all(1 <= b - a <= 3 for a, b in zip(levels, levels[1:])))


if __name__ == "__main__":
    with open("day_02_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
