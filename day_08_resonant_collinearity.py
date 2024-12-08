from collections import defaultdict
from itertools import combinations


def part_1(data):
    width, height = len(data[0]), len(data)
    antennae = defaultdict(list)
    for i, c in enumerate("".join(data)):
        if c != ".":
            antennae[c].append((i % width, i // width))
    antinodes = set()
    for locations in antennae.values():
        for (x1, y1), (x2, y2) in combinations(locations, r=2):
            dx, dy = (x1 - x2, y1 - y2)
            if 0 <= x1 + dx < width and 0 <= y1 + dy < height:
                antinodes.add((x1 + dx, y1 + dy))
            if 0 <= x2 - dx < width and 0 <= y2 - dy < height:
                antinodes.add((x2 - dx, y2 - dy))
    return len(antinodes)


def part_2(data):
    width, height = len(data[0]), len(data)
    antennae = defaultdict(list)
    for i, c in enumerate("".join(data)):
        if c != ".":
            antennae[c].append((i % width, i // width))
    antinodes = set()
    for locations in antennae.values():
        for (x1, y1), (x2, y2) in combinations(locations, r=2):
            dx, dy = (x1 - x2, y1 - y2)
            while 0 <= x1 < width and 0 <= y1 < height:
                antinodes.add((x1, y1))
                x1 += dx
                y1 += dy
            while 0 <= x2 < width and 0 <= y2 < height:
                antinodes.add((x2, y2))
                x2 -= dx
                y2 -= dy
    return len(antinodes)


if __name__ == "__main__":
    with open("day_08_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
