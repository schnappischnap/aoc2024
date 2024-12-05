from collections import defaultdict
from functools import cmp_to_key


def part_1(data):
    rules, updates = data.split("\n\n")
    rule = defaultdict(set)
    for line in rules.split():
        a, b = line.strip().split("|")
        rule[a].add(b)

    answer = 0
    for line in updates.split():
        update = line.strip().split(",")
        if not any (a in rule[b] for i, b in enumerate(update[1:], start=1)
                                 for a in update[0: i]):
            answer += int(update[len(update) // 2])
    return answer


def part_2(data):
    def cmp(a, b):
        if b in rule[a]:
            return -1
        return 0

    rules, updates = data.split("\n\n")
    rule = defaultdict(set)
    for line in rules.split():
        a, b = line.strip().split("|")
        rule[a].add(b)

    answer = 0
    for line in updates.split():
        update = line.strip().split(",")
        if any (a in rule[b] for i, b in enumerate(update[1:], start=1)
                             for a in update[0: i]):
            answer += int(sorted(update, key=cmp_to_key(cmp))[len(update) // 2])
    return answer


if __name__ == "__main__":
    with open("day_05_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
