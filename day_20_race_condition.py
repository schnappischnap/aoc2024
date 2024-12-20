def part_1(data):
    width = data.index("\n") + 1
    start = data.index("S") % width, data.index("S") // width
    path = set((x, y) for y, line in enumerate(data.splitlines())
                      for x, c in enumerate(line)
                      if c != "#")
    steps = {start: data.count(".")}
    queue = [start]
    while queue:
        x, y = queue.pop()
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if (nx, ny) in path and (nx, ny) not in steps:
                steps[(nx, ny)] = steps[(x, y)] - 1
                queue.append((nx, ny))

    return sum(steps[(x, y)] - steps[(nx, ny)] - 2 >= 100
               for x, y in steps.keys()
               for nx, ny in [(x+2, y), (x-2, y), (x, y-2), (x, y+2)]
               if (nx, ny) in steps)


def part_2(data):
    width = data.index("\n") + 1
    start = data.index("S") % width, data.index("S") // width
    path = set((x, y) for y, line in enumerate(data.splitlines())
                      for x, c in enumerate(line)
                      if c != "#")
    steps = {start: data.count(".")}
    queue = [start]
    while queue:
        x, y = queue.pop()
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if (nx, ny) in path and (nx, ny) not in steps:
                steps[(nx, ny)] = steps[(x, y)] - 1
                queue.append((nx, ny))

    return sum(steps[(x, y)] - steps[(nx, ny)] - distance >= 100
               for x, y in steps.keys()
               for nx, ny in steps.keys()
               if (distance := abs(x - nx) + abs(y - ny)) < 21)


if __name__ == "__main__":
    with open("day_20_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
