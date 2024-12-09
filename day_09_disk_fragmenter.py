from itertools import zip_longest


def part_1(data):
    blocks = []
    for i, (files, free_space) in enumerate(zip_longest(data[::2], data[1::2])):
        for _ in range(int(files)):
            blocks.append(i)
        if not free_space:
            continue
        for _ in range(int(free_space)):
            blocks.append(None)

    checksum = 0
    j = len(blocks)
    for i, block in enumerate(blocks):
        if i == j:
            return checksum
        if block is not None:
            checksum += block * i
        else:
            j -= 1
            while blocks[j] is None:
                if j == i:
                    return checksum
                j -= 1
            checksum += blocks[j] * i


def part_2(data):
    file_sizes = [int(size) for size in data[::2]]
    free_spaces = [int(size) for size in data[1::2]]

    checksum = 0
    i = 0
    evaluated = set()
    for id, size in enumerate(file_sizes):
        if id not in evaluated:
            checksum += sum(id * j for j in range(i, i + size))
            evaluated.add(id)
        i += size
        if id >= len(free_spaces):
            return checksum
        free_space = free_spaces[id]
        while free_space:
            for id2, size2 in reversed(list(enumerate(file_sizes))):
                if id2 in evaluated or size2 > free_space:
                    continue
                checksum += sum(id2 * j for j in range(i, i + size2))
                i += size2
                free_space -= size2
                evaluated.add(id2)
                if not free_space:
                    break
            else:
                break
        i += free_space


if __name__ == "__main__":
    with open("day_09_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
