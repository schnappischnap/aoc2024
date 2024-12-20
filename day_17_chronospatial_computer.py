import re


def part_1(data):
    a, b, c, *program = map(int, re.findall(r"\d+", data))
    return ",".join((str(v) for v in run_program(a, b, c, program)))


def part_2(data):
    _, b, c, *program = map(int, re.findall(r"\d+", data))
    queue = [(0, 1)]
    while queue:
        previous_a, index = queue.pop(0)
        for a in range(previous_a, previous_a + 8):
            if run_program(a, b, c, program) == program[-index:]:
                if index == len(program):
                    return a
                queue.append((a * 8, index + 1))


def run_program(a, b, c, program):
    i = 0
    output = []
    while i < len(program) - 1:
        opcode = program[i]
        operand = program[i+1]
        combo = [0, 1, 2, 3, a, b, c]
        match opcode:
            case 0: a //= 2 ** combo[operand]
            case 1: b ^= operand
            case 2: b = combo[operand] % 8
            case 3: i = operand - 2 if a else i
            case 4: b ^= c
            case 5: output.append(combo[operand] % 8)
            case 6: b = a // 2 ** combo[operand]
            case 7: c = a // 2 ** combo[operand]
        i += 2
    return output


if __name__ == "__main__":
    with open("day_17_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
