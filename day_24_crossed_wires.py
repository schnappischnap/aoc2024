import operator


def part_1(data):
    LOGIC = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor}
    wire_values, gate_connections = data.split("\n\n")
    wires = {line[:3]: int(line[-1]) for line in wire_values.splitlines()}
    queue = [line.split(" ") for line in gate_connections.splitlines()]
    while queue:
        a, op, b, _, c = queue.pop(0)
        if a not in wires or b not in wires:
            queue.append((a, op, b, _, c))
            continue
        wires[c] = LOGIC[op](wires[a], wires[b])
    return int("".join(str(wires[f"z{i:02}"])
                       for i in reversed(range(100))
                       if f"z{i:02}" in wires), 2)


if __name__ == "__main__":
    with open("day_24_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
