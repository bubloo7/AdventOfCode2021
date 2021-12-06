input = open("Day 2/input")

arr = input.read().split('\n')


depth = 0
pos = 0
for i in range(len(arr)):
    split = arr[i].split(" ")

    if split[0] == "up":
        depth -= int(split[1])
    if split[0] == "down":
        depth += int(split[1])
    if split[0] == "forward":
        pos += int(split[1])

ans = depth*pos
print(ans) # answer is 1893605
