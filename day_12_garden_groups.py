def part_1(data):
    width, height = len(data[0]), len(data)
    seen = set()

    def flood(start):
        x, y = start
        plant = data[y][x]
        perimeter = 0
        area = 0
        stack = [start]
        while stack:
            x, y = stack.pop()
            area += 1
            perimeter += sum(nx < 0 or nx >= width or ny < 0 or ny >= height or data[ny][nx] != plant 
                             for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if (nx, ny) not in seen and 0 <= nx < width and 0 <= ny < height and data[ny][nx] == plant:
                    stack.append((nx, ny))
                    seen.add((nx, ny))
        return area, perimeter
    
    cost = 0
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if (x, y) in seen: 
                continue
            seen.add((x, y))
            a, p = flood((x, y))
            cost += a * p
    return cost
            

def part_2(data):
    data = (["." * (len(data[0]) + 2)] + 
            ["." + line + "." for line in data] + 
            ["." * (len(data[0]) + 2)])
    seen = set()

    def flood(start):
        x, y = start
        plant = data[y][x]
        corners = 0
        area = 0
        stack = [start]
        while stack:
            x, y = stack.pop()
            area += 1

            plant_sides = (data[y][x-1] == plant) + (data[y-1][x] == plant)
            if (plant_sides == 0) or (plant_sides == 2 and data[y-1][x-1] != plant):
                corners += 1
            plant_sides = (data[y-1][x] == plant) + (data[y][x+1] == plant)
            if (plant_sides == 0) or (plant_sides == 2 and data[y-1][x+1] != plant):
                corners += 1
            plant_sides = (data[y][x+1] == plant) + (data[y+1][x] == plant)
            if (plant_sides == 0) or (plant_sides == 2 and data[y+1][x+1] != plant):
                corners += 1
            plant_sides = (data[y+1][x] == plant) + (data[y][x-1] == plant)
            if (plant_sides == 0) or (plant_sides == 2 and data[y+1][x-1] != plant):
                corners += 1

            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if (nx, ny) not in seen and data[ny][nx] == plant:
                    stack.append((nx, ny))
                    seen.add((nx, ny))

        return area, corners
    
    cost = 0
    for y, line in enumerate(data[1:-1], start=1):
        for x, c in enumerate(line[1:-1], start=1):
            if (x, y) in seen: 
                continue
            seen.add((x, y))
            area, sides = flood((x, y))
            cost += area * sides
    return cost


if __name__ == "__main__":
    with open("day_12_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
