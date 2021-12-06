input = open("Day 2/input")

arr = input.read().split('\n')

depth = 0
aim = 0
pos = 0
for i in range(len(arr)):
    split = arr[i].split(" ")

    if split[0] == "up":
        aim -= int(split[1])
    if split[0] == "down":
        aim += int(split[1])
    if split[0] == "forward":
        pos += int(split[1])
        depth += aim *int(split[1])

ans = depth*pos
print(ans) # answer is 2120734350
