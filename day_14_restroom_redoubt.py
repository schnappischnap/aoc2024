import math
import re


def part_1(data):
    width, height = 101, 103
    robots = [re.findall(r"-?\d+", line) for line in data]
    safety_factors = [0, 0, 0, 0]
    for robot in robots:
        x, y, dx, dy = map(int, robot)
        nx, ny = (x + dx * 100) % width, (y + dy * 100) % height
        if nx == width // 2 or ny == height // 2:
            continue
        safety_factors[(nx > width // 2) + (ny > height // 2) * 2] += 1
    return math.prod(safety_factors)


def part_2(data):
    width, height = 101, 103
    robots = [re.findall(r"-?\d+", line) for line in data]
    seen = set()
    for i in range(10000):
        positions = set()
        for j, robot in enumerate(robots):
            x, y, dx, dy = map(int, robot)
            nx, ny = (x + dx * i) % width, (y + dy * i) % height
            positions.add((nx, ny))
        if len(positions) == len(robots):
            return i


if __name__ == "__main__":
    with open("day_14_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
