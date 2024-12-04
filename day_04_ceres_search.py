def part_1(data):
    height, width = len(data), len(data[0])
    data = "".join(line for line in data)
    count = 0
    for y in range(height):
        for x in range(width):
            count += data[y * width + x: (y+4) * width + x: width] in ("XMAS", "SAMX")
            if x < width - 3:
                count += data[y * width + x: y * width + x + 4] in ("XMAS", "SAMX")
                count += data[y * width + x: (y+4) * width + x + 4: width + 1] in ("XMAS", "SAMX")
            if x >= 3:
                count += data[y * width + x: (y+4) * width + x - 4: width - 1] in ("XMAS", "SAMX")
    return count


def part_2(data):
    height, width = len(data), len(data[0])
    data = "".join(line for line in data)
    count = 0
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            if data[y * width + x] != "A":
                continue
            count += "".join((data[(y - 1) * width + x - 1], 
                              data[(y - 1) * width + x + 1], 
                              data[(y + 1) * width + x - 1], 
                              data[(y + 1) * width + x + 1])) in ["MMSS", "SSMM", "MSMS", "SMSM"]
    return count


if __name__ == "__main__":
    with open("day_04_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
