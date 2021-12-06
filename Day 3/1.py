input = open("Day 3/input")

arr = input.read().split("\n")

for i in range(len(arr)):
    arr[i] = int(arr[i],2)


gamma = 0
mask = 2048

# bit manipulations are fun :) 

for i in range(12):
    count0 = 0
    count1 = 0
    for j in range(len(arr)):
        if arr[j] & mask == 0:
            count0 += 1
        else:
            count1 += 1
    
    
    if count0 < count1:
        gamma |= mask

    mask >>= 1

epsilon = 4095 ^ gamma

ans = gamma * epsilon
print(ans) # answer is 775304
