def part_1(data):
    start = (0, 0)
    end = (70, 70)
    corrupted = set(tuple(map(int, line.split(","))) for line in data[:1024])
    return dfs(start, end, corrupted)


def part_2(data):
    start = (0, 0)
    end = (70, 70)
    corrupted = set(tuple(map(int, line.split(","))) for line in data[:1024])
    for i in range(1024, 3451):
        position = tuple(map(int, data[i].split(",")))
        corrupted.add(position)
        if not dfs(start, end, corrupted):
            return ",".join(str(v) for v in position)


def dfs(start, end, corrupted):
    queue = [(start, 0)]
    seen = set()
    while queue:
        (x, y), steps = queue.pop(0)
        if (x, y) == end:
            return steps
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if (nx, ny) in corrupted:
                continue
            if (nx, ny) in seen:
                continue
            if not 0 <= nx <= 70 or not 0 <= ny <= 70:
                continue
            queue.append(((nx, ny), steps + 1))
            seen.add((nx, ny))
    return False


if __name__ == "__main__":
    with open("day_18_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
