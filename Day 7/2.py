input = open("Day 7/input")

arr = [int(x) for x in input.read().split(",")]

hmap = {}

for i in arr:
    hmap[i] = hmap.get(i,0) + 1

ans = 1000000000
for i in range(min(arr), max(arr)):
    temp = 0
    for j in hmap:
        n = abs(j - i)
        temp += n*(n+1)*hmap[j]/2
    
    ans = min(ans,temp)

print(int(ans)) # answer is 99266250
