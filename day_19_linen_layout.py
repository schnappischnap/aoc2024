from functools import cache


def part_1(data):
    @cache
    def possible(design):
        return design == "" or any(possible(design.removeprefix(p))
                                   for p in patterns if design.startswith(p))

    patterns = data[0].strip().split(", ")
    return sum(possible(design.strip()) for design in data[2:])


def part_2(data):
    @cache
    def possiblities(design):
        return design == "" or sum(possiblities(design.removeprefix(p))
                                   for p in patterns if design.startswith(p))

    patterns = data[0].strip().split(", ")
    return sum(possiblities(design.strip()) for design in data[2:])


if __name__ == "__main__":
    with open("day_19_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
