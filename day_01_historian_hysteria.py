from collections import Counter


def part_1(data):
    left, right = zip(*[map(int, line.split()) for line in data])
    return sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))


def part_2(data):
    left, right = zip(*[map(int, line.split()) for line in data])
    counter = Counter(right)
    return sum(l * counter[l] for l in left)


if __name__ == "__main__":
    with open("day_01_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
