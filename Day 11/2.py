arr = [[int(i) for i in ar] for ar in [list(c) for c in open("Day 11/input").read().split('\n')]]


def getNeighbors(arr, i, j):
    ans = []
    if i >= 1:
        ans.append((i-1, j))
    if i < len(arr) - 1:
        ans.append((i+1, j))
    if j >= 1:
        ans.append((i, j-1))
    if j < len(arr[0]) - 1:
        ans.append((i, j+1))

    if i >= 1 and j >= 1:
        ans.append((i-1,j-1))
    if i < len(arr) - 1 and j >= 1:
        ans.append((i+1,j-1))
    if i >= 1 and j < len(arr[0]) - 1:
        ans.append((i-1,j+1))
    if i < len(arr) - 1 and j < len(arr[0]) - 1:
        ans.append((i+1,j+1))

    return ans

ans = 0
good = True
while good:
    flashed = False
    first = True
    for i in range(len(arr)):
            for j in range(len(arr[0])):
                arr[i][j] += 1
    
    counter = 0
    while first or flashed:
        first = False
        flashed = False
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] > 9:
                    flashed = True
                    arr[i][j] = 0
                    counter += 1
                    for i2,j2 in getNeighbors(arr, i, j):
                        if arr[i2][j2] != 0: 
                            arr[i2][j2] += 1

    
        if counter == 100:
            good = False

    ans += 1

print(ans) # answer is 505
