def part1(level: list[str]) -> bool:
    if len(level) == 2:
        return True
    increase = True
    decrease = True
    for index, number in enumerate(level):
        try:
            diff = int(level[index + 1]) - int(number)
            if abs(diff) > 3 or abs(diff) < 1:
                return False
            if diff > 0:
                decrease = False
            if diff < 0:
                increase = False
        except IndexError:
            continue
    return increase or decrease


def part2(level: list[str]) -> bool:
    if part1(level):
        return True
    for index in range(len(level)):
        modified = level.copy()
        modified.pop(index)
        if part1(modified):
            return True
    return False


if __name__ == "__main__":
    p1: int = 0
    p2: int = 0
    with open("puzzle.txt", "r") as puzzle:
        for line in puzzle.readlines():
            level = line.strip().split()
            p1 += part1(level)
            p2 += part2(level)

    print("p1:", p1)
    print("p2:", p2)
