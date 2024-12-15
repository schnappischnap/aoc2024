def part_1(data):
    layout, moves = data.split("\n\n")
    width = layout.index("\n") + 1
    x, y = data.index("@") % width, data.index("@") // width
    layout = [list(line) for line in layout.splitlines()]
    delta = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
    for move in moves:
        if move not in delta:
            continue
        dx, dy = delta[move]
        nx, ny = x + dx, y + dy
        while layout[ny][nx] == "O":
            nx, ny = nx + dx, ny + dy
        if layout[ny][nx] == "#":
            continue
        layout[y][x] = "."
        layout[y+dy][x+dx] = "@"
        if (nx, ny) != (x+dx, y+dy):
            layout[ny][nx] = "O"
        x, y = x + dx, y + dy
    return sum(y * 100 + x 
               for y, line in enumerate(layout)
               for x, c in enumerate(line)
               if c == "O")


def part_2(data):
    layout, moves = data.split("\n\n")
    layout = layout.replace(".", "..").replace(
        "#", "##").replace("O", "[]").replace("@", "@.")
    width = layout.index("\n") + 1
    x, y = layout.index("@") % width, layout.index("@") // width
    layout = [list(line) for line in layout.splitlines()]
    delta = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
    for move in moves:
        if move not in delta:
            continue
        dx, dy = delta[move]
        if layout[y+dy][x+dx] == "#":
            continue
        to_move = [(x, y)]
        to_check = [(x + dx, y + dy)]
        checked = set()
        while to_check:
            nx, ny = to_check.pop()
            if (nx, ny) in checked:
                continue
            checked.add((nx, ny))
            if layout[ny][nx] == "[":
                to_move.append((nx, ny))
                to_move.append((nx+1, ny))
                to_check.append((nx+dx, ny+dy))
                to_check.append((nx+1+dx, ny+dy))
            elif layout[ny][nx] == "]":
                to_move.append((nx, ny))
                to_move.append((nx-1, ny))
                to_check.append((nx+dx, ny+dy))
                to_check.append((nx-1+dx, ny+dy))
            elif layout[ny][nx] == "#":
                to_move = []
                break
        if not to_move:
            continue
        new_layout = [line[:] for line in layout]
        for nx, ny in to_move:
            new_layout[ny][nx] = "."
        for nx, ny in to_move:
            new_layout[ny+dy][nx+dx] = layout[ny][nx]
        layout = new_layout
        x, y = x+dx, y+dy
    return sum(y * 100 + x 
               for y, line in enumerate(layout)
               for x, c in enumerate(line)
               if c == "[")


if __name__ == "__main__":
    with open("day_15_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
