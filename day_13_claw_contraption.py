import re
import z3
from itertools import product


def part_1(data):
    def find_tokens(a, b, prize):
        for i, j in product(range(100), repeat=2):
            x0, y0 = a
            x1, y1 = b
            value = (x0 * i + x1 * j, y0 * i + y1 * j)
            if value == prize:
                return i * 3 + j
        return 0

    tokens = 0
    for machine in data.split("\n\n"):
        a, b, prize = [tuple(int(v) for v in tup)
                       for tup in re.findall(r"X.(\d+), Y.(\d+)", machine)]
        tokens += find_tokens(a, b, prize)
    return tokens


def part_2(data):
    tokens = 0
    for machine in data.split("\n\n"):
        values = [int(v) for v in re.findall(r"(\d+)", machine)]
        a = z3.Int("a")
        b = z3.Int("b")
        solver = z3.Solver()
        solver.add(values[0] * a + values[2] * b == values[4] + 10000000000000)
        solver.add(values[1] * a + values[3] * b == values[5] + 10000000000000)
        if solver.check() == z3.sat:
            tokens += solver.model()[a].as_long() * 3 + solver.model()[b].as_long()
    return tokens


if __name__ == "__main__":
    with open("day_13_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
