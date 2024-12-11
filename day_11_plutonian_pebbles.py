from collections import Counter


def part_1(data):
    stones = [int(i) for i in data.split()]
    for _ in range(25):
        new_stones = []
        for i, stone in enumerate(stones):
            if stone == 0:
                new_stones.append(1)
            elif len(s := str(stone)) % 2 == 0:
                new_stones.append(int(s[:len(s) // 2]))
                new_stones.append(int(s[len(s) // 2:]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)


def part_2(data):
    stones = Counter([int(i) for i in data.split()])
    for _ in range(75):
        new_stones = Counter()
        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
            elif len(s := str(stone)) % 2 == 0:
                new_stones[int(s[:len(s) // 2])] += count
                new_stones[int(s[len(s) // 2:])] += count
            else:
                new_stones[stone * 2024] += count
        stones = new_stones
    return stones.total()


if __name__ == "__main__":
    with open("day_11_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
