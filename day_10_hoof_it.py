def part_1(data):
    def dfs(start):
        summits = set()
        stack = [(start, 0)]
        while stack:
            (x, y), h = stack.pop()
            if h == 9:
                summits.add((x, y))
                continue
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < width and 0 <= ny < height and int(data[ny][nx]) == h + 1:
                    stack.append(((nx, ny), h+1))
        return len(summits)

    width, height = len(data[0]), len(data)
    return sum(dfs((x, y)) for y in range(height) for x in range(width) if data[y][x] == "0")


def part_2(data):
    def dfs(start):
        score = 0
        stack = [(start, 0)]
        while stack:
            (x, y), h = stack.pop()
            if h == 9:
                score += 1
                continue
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < width and 0 <= ny < height and int(data[ny][nx]) == h + 1:
                    stack.append(((nx, ny), h+1))
        return score

    width, height = len(data[0]), len(data)
    return sum(dfs((x, y)) for y in range(height) for x in range(width) if data[y][x] == "0")


if __name__ == "__main__":
    with open("day_10_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
