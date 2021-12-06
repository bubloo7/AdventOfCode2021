input = open("Day 6/input")

arr = input.read().split(',')
arr = [int(x) for x in arr]

count = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for elem in arr:
    count[elem] += 1

new =  [0, 0, 0, 0, 0, 0, 0, 0, 0]
for day in range(256):
    new =  [0, 0, 0, 0, 0, 0, 0, 0, 0]
    new[6] = count[0]
    new[8] = count[0]
    for i in range(0,len(new)-1):
        new[i] += count[i+1]

    count = new

ans = sum(count)
print(ans) # answer is 1631647919273