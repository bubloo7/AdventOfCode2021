input = open("Day 1/input", 'r')
arr = input.read().split('\n')

for i in range(len(arr)):
    arr[i] = int(arr[i])

rsum = arr[0] + arr[1] + arr[2]
ans = 0
for i in range(3, len(arr)):
    currsum = rsum + arr[i] - arr[i-3]
    if currsum > rsum:
        ans += 1
    rsum = currsum        

print(ans) # answer is 1150
