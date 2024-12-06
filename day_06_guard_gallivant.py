def part_1(data):
    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == "^":
                x, y = j, i
    height, width = len(data), len(data[0])
    dx, dy = (0, -1)
    positions = set([(x, y)])

    while 0 <= x + dx < width and 0 <= y + dy < height:
        if data[y + dy][x + dx] == "#":
            dx, dy = -dy, dx
        else:
            x, y = x + dx, y + dy
            positions.add((x, y))
    return len(positions)


def part_2(data):
    def creates_loop(pos, delta):
        (x, y), (dx, dy) = pos, delta
        obstacle = (x + dx, y + dy)
        visited = set([(x, y, dx, dy)])
        while 0 <= x + dx < width and 0 <= y + dy < height:
            if data[y + dy][x + dx] == "#" or (x + dx, y + dy) == obstacle:
                dx, dy = -dy, dx
            else:
                x, y = x + dx, y + dy
                if (x, y, dx, dy) in visited:
                    return True
                visited.add((x, y, dx, dy))
        return False

    for i, line in enumerate(data):
        for j, c in enumerate(line):
            if c == "^":
                x, y = j, i
    height, width = len(data), len(data[0])
    dx, dy = (0, -1)
    loops = set()
    visited = set((x, y))
    while 0 <= x + dx < width and 0 <= y + dy < height:
        if data[y + dy][x + dx] == "#":
            dx, dy = -dy, dx
        else:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and creates_loop((x, y), (dx, dy)):
                loops.add((nx, ny))
            x, y = nx, ny
            visited.add((x, y))
    return len(loops)


if __name__ == "__main__":
    with open("day_06_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
