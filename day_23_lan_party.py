from collections import defaultdict
from itertools import combinations


def part_1(data):
    connections = defaultdict(set)
    for line in data:
        a, b = line[:2], line[3:5]
        connections[a].add(b)
        connections[b].add(a)

    groups = set()
    for computer in connections:
        if not computer.startswith("t"):
            continue
        for other1, other2 in combinations(connections[computer], 2):
            if other1 in connections[other2]:
                groups.add(tuple(sorted((computer, other1, other2))))
    return len(groups)


def part_2(data):
    connections = defaultdict(set)
    for line in data:
        a, b = line[:2], line[3:5]
        connections[a].add(b)
        connections[b].add(a)
    
    groups = set()
    for computer in connections:
        for i in range(len(connections[computer])):
            for others in combinations(connections[computer], i):
                if all(other1 in connections[other2] for other1, other2 in combinations(others, 2)):
                    groups.add(tuple(sorted((computer, *others))))
    return ",".join(max(groups, key=len))


if __name__ == "__main__":
    with open("day_23_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
