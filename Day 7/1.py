input = open("Day 7/input")

arr = [int(x) for x in input.read().split(",")]

hmap = {}

for i in arr:
    hmap[i] = hmap.get(i,0) + 1


ans = 1000000000
for i in hmap:
    temp = 0
    for j in hmap:
        temp += abs(j - i)*hmap[j]
    
    ans = min(ans,temp)

print(ans) # answer is 352331
