left_list = []
right_list = []

with open("puzzle.txt", "r") as puzzle:
    for line in puzzle.readlines():
        temp = line.split()
        left_list.append(temp[0])
        right_list.append(temp[1].rstrip())

result = 0

while left_list:
    left_number = left_list.pop(0)
    many = list(filter(lambda right_number: right_number == left_number, right_list))
    result += int(left_number) * len(many)

print(result)
