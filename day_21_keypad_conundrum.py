from functools import cache
import math


def part_1(data):
    def create_code(code):
        x, y = directional_keypad["A"]
        new_code = ""
        for c in code:
            nx, ny = directional_keypad[c]
            dx, dy = nx - x, ny - y
            if dy < 0:
                new_code += ("<" if dx < 0 else ">") * abs(dx) + "^" * abs(dy) + "A"
            else:
                new_code += "v" * abs(dy) + ("<" if dx < 0 else ">") * abs(dx) + "A"
            x, y = directional_keypad[c]
        return new_code
    
    directional_keypad = {c: (i % 3, i // 3) for i, c in enumerate("X^A<v>")}
    numerical_keypad = {c: (i % 3, i // 3) for i, c in enumerate("789456123X0A")}

    x, y = numerical_keypad["A"]
    result = 0
    for keypad_code in data:
        cost = 0
        for c in keypad_code:
            nx, ny = numerical_keypad[c]
            dx, dy = nx - x, ny - y
            if x == 0 and ny == 3:
                codes = [">" * abs(dx) + "v" * abs(dy) + "A"]
            elif y == 3 and nx == 0:
                codes = ["^" * abs(dy) + "<" * abs(dx) + "A"]
            else:
                codes = [("^" if dy < 0 else "v") * abs(dy) + ("<" if dx < 0 else ">") * abs(dx) + "A",
                         ("<" if dx < 0 else ">") * abs(dx) + ("^" if dy < 0 else "v") * abs(dy) + "A"]
            for _ in range(2):
                codes = [create_code(code) for code in codes]
            cost += len(min(codes, key=len))
            x, y = nx, ny
        result += cost * int(keypad_code[:3])
    return result


def part_2(data):
    @cache
    def code_cost(code, robots=25):
        if robots == 0:
            return len(code)
        result = 0
        x, y = directional_keypad["A"]
        for c in code:
            nx, ny = directional_keypad[c]
            result += cheapest_path(x, y, nx, ny, robots)
            x, y = nx, ny
        return result
    
    @cache
    def cheapest_path(x, y, nx, ny, robots=25):
        result = math.inf
        queue = [(x, y, "")]
        while queue:
            x, y, path = queue.pop(0)
            if (x, y) == (0, 0):
                continue
            if (x, y) == (nx, ny):
                robot = code_cost(path + "A", robots - 1)
                result = min(result, robot)
            else:
                if nx < x:
                    queue.append((x - 1, y, path + "<"))
                elif nx > x:
                    queue.append((x + 1, y, path + ">"))
                if ny < y:
                    queue.append((x, y - 1, path + "^"))
                elif ny > y:
                    queue.append((x, y + 1, path + "v"))
        return result
    
    directional_keypad = {c: (i % 3, i // 3) for i, c in enumerate("X^A<v>")}
    numerical_keypad = {c: (i % 3, i // 3) for i, c in enumerate("789456123X0A")}

    x, y = numerical_keypad["A"]
    result = 0
    for keypad_code in data:
        cost = 0
        for c in keypad_code:
            nx, ny = numerical_keypad[c]
            dx, dy = nx - x, ny - y
            if x == 0 and ny == 3:
                codes = [">" * abs(dx) + "v" * abs(dy) + "A"]
            elif y == 3 and nx == 0:
                codes = ["^" * abs(dy) + "<" * abs(dx) + "A"]
            else:
                codes = [("^" if dy < 0 else "v") * abs(dy) + ("<" if dx < 0 else ">") * abs(dx) + "A",
                         ("<" if dx < 0 else ">") * abs(dx) + ("^" if dy < 0 else "v") * abs(dy) + "A"]
            cost += min(code_cost(code) for code in codes)
            x, y = nx, ny
        result += cost * int(keypad_code[:3])
    return result


if __name__ == "__main__":
    with open("day_21_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
