import math


def part_1(data):
    width = data.index("\n") + 1
    start = data.index("S") % width, data.index("S") // width
    goal = data.index("E") % width, data.index("E") // width
    layout = data.splitlines()

    best_score = math.inf
    seen = dict()
    queue = [(start, (1, 0), 0)]
    while queue:
        (x, y), (dx, dy), score = queue.pop(0)
        if (x, y) == goal:
            best_score = min(best_score, score)
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            ndx, ndy = nx - x, ny - y
            nscore = score + (1 if (ndx, ndy) == (dx, dy) else 1001)
            if layout[ny][nx] == "#" or nscore > seen.get(((nx, ny), (ndx, ndy)), math.inf):
                continue
            seen[(((nx, ny), (ndx, ndy)))] = nscore
            queue.append(((nx, ny), (ndx, ndy), nscore))
    return best_score


def part_2(data):
    width = data.index("\n") + 1
    start = data.index("S") % width, data.index("S") // width
    goal = data.index("E") % width, data.index("E") // width
    layout = data.splitlines()

    best_score = math.inf
    best_seats = set()
    seen = dict()
    queue = [(start, (1, 0), 0, [start])]
    while queue:
        (x, y), (dx, dy), score, path = queue.pop(0)
        if (x, y) == goal:
            if score == best_score:
                best_seats.update(path)
            if score < best_score:
                best_score = score
                best_seats = set(path)
        for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            ndx, ndy = nx - x, ny - y
            nscore = score + (1 if (ndx, ndy) == (dx, dy) else 1001)
            if layout[ny][nx] == "#" or nscore > seen.get(((nx, ny), (ndx, ndy)), math.inf):
                continue
            seen[(((nx, ny), (ndx, ndy)))] = nscore
            queue.append(((nx, ny), (ndx, ndy), nscore, path + [(nx, ny)]))
    return len(best_seats)


if __name__ == "__main__":
    with open("day_16_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
