input = open("Day 8/lolakil")

arr = input.read().split("\n")

ans = 0

for i in arr:
    curr = i.split(' ')
    for j in range(11, 15):
        if len(curr[j]) == 2 or len(curr[j]) == 4 or len(curr[j]) == 3 or len(curr[j]) == 7:
            ans += 1

print(ans)  # answer is 247
