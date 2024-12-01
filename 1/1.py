left_list = []
right_list = []

with open("puzzle.txt", "r") as puzzle:
    for line in puzzle.readlines():
        temp = line.split()
        left_list.append(temp[0])
        right_list.append(temp[1].rstrip())

left_list.sort()
right_list.sort()

result = 0

while left_list:
    left_number = int(left_list.pop(0))
    right_number = int(right_list.pop(0))
    result += abs(left_number - right_number)

print(result)
