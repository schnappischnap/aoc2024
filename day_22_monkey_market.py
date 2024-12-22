from collections import deque, Counter
from functools import reduce


def part_1(data):
    return sum(reduce(lambda v, _: step(v), range(2000), int(line)) for line in data)


def part_2(data):
    total_bananas = Counter()
    for line in data:
        changes = deque(maxlen=4)
        bananas = dict()
        previous_value, value = int(line), step(int(line))
        for i in range(1999):
            previous_value, value = value, step(value)
            changes.append((value % 10) - (previous_value % 10))
            if (key := tuple(changes)) not in bananas:
                bananas[key] = value % 10
        total_bananas.update(bananas)
    return total_bananas.most_common(1)[0][1]


def step(value):
    value = ((value * 64) ^ value) % 16777216
    value = ((value // 32) ^ value) % 16777216
    value = ((value * 2048) ^ value) % 16777216
    return value


if __name__ == "__main__":
    with open("day_22_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
