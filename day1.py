def part1(left_list: list[str], right_list: list[str]) -> int:
    result = 0
    while left_list:
        left_number = int(left_list.pop(0))
        right_number = int(right_list.pop(0))
        result += abs(left_number - right_number)
    return result


def part2(left_list: list[str], right_list: list[str]) -> int:
    result = 0

    while left_list:
        left_number = left_list.pop(0)
        many = list(
            filter(lambda right_number: right_number == left_number, right_list)
        )
        result += int(left_number) * len(many)
    return result


if __name__ == "__main__":
    left_list: list[str] = []
    right_list: list[str] = []
    p1: int = 0
    p2: int = 0
    with open("puzzle.txt", "r") as puzzle:
        for line in puzzle.readlines():
            left, right = line.strip().split()
            left_list.append(left)
            right_list.append(right)

    left_list.sort()
    right_list.sort()

    p1 = part1(left_list.copy(), right_list.copy())
    p2 = part2(left_list.copy(), right_list.copy())

    print("p1:", p1)
    print("p2:", p2)
