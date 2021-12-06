input = open("Day 3/input")

arr = input.read().split("\n")

oxy = []
carb = []

for i in range(len(arr)):
    oxy.append( int(arr[i],2))
    carb.append(int(arr[i],2))



gamma = 0
mask = 2048


temp1 = -1
temp2 = 1
for i in range(12):
    count0 = 0
    count1 = 0
    for j in range(len(oxy)):
        if oxy[j] & mask == 0:
            count0 += 1
        else:
            count1 += 1

    if count0 <= count1:
        for j in range(len(oxy) -1,-1,-1):
            if oxy[j] & mask == 0:
                oxy.pop(j)
                if len(oxy) == 1:
                    temp1 = oxy[0]
    
    else:
        for j in range(len(oxy) -1, -1,-1):
            if oxy[j] & mask != 0:
                oxy.pop(j)
                if len(oxy) == 1:
                    temp1 = oxy[0]

    count0 = 0
    count1 = 0
    
    for j in range(len(carb)):
        if carb[j] & mask == 0:
            count0 += 1
        else:
            count1 += 1

    if count0 <= count1:
        for j in range(len(carb)-1, -1,-1):
            if carb[j] & mask != 0:
                carb.pop(j)
                if len(carb) == 1:
                    temp2 = carb[0]
    
    else:
        for j in range(len(carb)-1 , -1,-1):
            if carb[j] & mask == 0:
                carb.pop(j)
                if len(carb) == 1:
                    temp2 = carb[0]

    mask >>= 1

ans = temp1 * temp2
print(ans) # answer is 1370737
