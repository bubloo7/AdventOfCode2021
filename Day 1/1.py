input = open("Day 1/input", 'r')
arr = input.read().split('\n')
ans = 0
for i in range(1,len(arr)):
    if int(arr[i]) > int(arr[i -1]):
        ans += 1

print(ans) # answer is 1215
