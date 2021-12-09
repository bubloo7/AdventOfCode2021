input = open('Day 9/input')
temp = input.read()
arr = [[int(i) for i in ar] for ar in [list(c) for c in temp.split('\n')]]

dumNum = -1


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

    return ans


def isLowPoint(arr, i, j):
    curr = arr[i][j]

    if i >= 1 and curr >= arr[i-1][j]:
        return False
    if i < len(arr)-1 and curr >= arr[i+1][j]:
        return False
    if j >= 1 and curr >= arr[i][j - 1]:
        return False
    if j < len(arr[0])-1 and curr >= arr[i][j+1]:
        return False

    return True


lowPoints = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if isLowPoint(arr, i, j):
            lowPoints.append((i, j))

basins = []
for i in range(len(arr)):
    temp = []
    for j in range(len(arr[0])):
        temp.append(dumNum)
    basins.append(temp)


sizes = []
currC = 0

for lp in lowPoints:
    q = []
    q.append(lp)

    s = 0

    while len(q) != 0:
        i2, j2 = q.pop(0)

        if basins[i2][j2] != dumNum or arr[i2][j2] == 9:
            continue

        basins[i2][j2] = currC
        s += 1

        for nneb in getNeighbors(arr, i2, j2):
            q.append(nneb)

    sizes.append(s)
    currC += 1

sizes = sorted(sizes)
print(sizes[-3] * sizes[-2] * sizes[-1]) # answer is 949905
