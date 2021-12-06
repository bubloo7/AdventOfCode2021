input = open("Day 5/input")

arr = input.read().split('\n')

edges = []
hor_or_ver = []
for line in arr:
    line = line.replace(" -> ", ",")
    nums = line.split(',')
    if nums[0] == nums[2] or nums[1] == nums[3]:
        hor_or_ver.append([(int(nums[0]),  int(nums[1])), (int(nums[2]), int(nums[3]))])
    else:
        edges.append([(int(nums[0]),  int(nums[1])), (int(nums[2]), int(nums[3]))])
    

floor = [ [ 0 for y in range( 1000 ) ] for x in range( 1000 ) ]

test = 0
for tup in hor_or_ver:
    for i in range(tup[0][0], tup[1][0] + 1):
        for j in range(tup[0][1], tup[1][1] + 1):
            floor[j][i] += 1
    for i in range(tup[0][0], tup[1][0] - 1, -1):
        for j in range(tup[0][1], tup[1][1] - 1,-1):
            floor[j][i] += 1

ans = 0
for arrr in floor:
    for eelem in arrr:
        if eelem > 1:
            ans += 1

print(ans) # Answer is 5608
