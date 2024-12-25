def part_1(data):
    locks = [tuple(column.index(".") for column in zip(*schematic.splitlines()))
             for schematic in data.split("\n\n")
             if schematic.startswith("#####")]
    keys = [tuple(column.index("#") for column in zip(*schematic.splitlines()))
            for schematic in data.split("\n\n")
            if schematic.startswith(".....")]

    return sum(sum(all(l < 1 + k for k, l in zip(key, lock)) for key in keys) for lock in locks)


if __name__ == "__main__":
    with open("day_25_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
