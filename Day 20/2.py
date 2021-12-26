input = open('Day 20/input').read().splitlines()

def getVal(arr, i, j, algo):
    ans = 0

    if i >= 1 and j >= 1 and arr[i-1][j-1] == '#':
        ans |= 256

    if i >= 1 and arr[i-1][j] == '#':
        ans |= 128

    if i >= 1 and j < len(arr[0]) - 1 and arr[i-1][j+1] == '#':
        ans |= 64

    if j >= 1 and arr[i][j-1] == '#':
        ans |= 32

    if arr[i][j] == '#':
        ans |= 16
    if j < len(arr[0]) - 1 and arr[i][j+1] == '#':
        ans |= 8

    if i < len(arr) - 1 and j >= 1 and arr[i+1][j-1] == '#':
        ans |= 4
    if i < len(arr) - 1 and arr[i+1][j] == '#':
        ans |= 2
    if i < len(arr) - 1 and j < len(arr[0]) - 1 and arr[i+1][j+1] == '#':
        ans |= 1

    return algo[ans]


def getVal2(arr, i, j, algo):

    ans = 0

    if not (i >= 1 and j >= 1) or arr[i-1][j-1] == '#':
        ans |= 256

    if not (i >= 1) or arr[i-1][j] == '#':
        ans |= 128

    if not (i >= 1 and j < len(arr[0]) - 1) or arr[i-1][j+1] == '#':
        ans |= 64

    if not j >= 1 or arr[i][j-1] == '#':
        ans |= 32

    if arr[i][j] == '#':
        ans |= 16
    if not (j < len(arr[0]) - 1) or arr[i][j+1] == '#':
        ans |= 8

    if not (i < len(arr) - 1 and j >= 1) or arr[i+1][j-1] == '#':
        ans |= 4
    if not (i < len(arr) - 1) or arr[i+1][j] == '#':
        ans |= 2
    if not (i < len(arr) - 1 and j < len(arr[0]) - 1) or arr[i+1][j+1] == '#':
        ans |= 1

    return algo[ans]


algo = input[0]

curr = []
for i in range(2, len(input)):
    curr.append(list(input[i]))


for step in range(50):
    thing = '.' if step % 2 == 0 else '#'
    print(step)
    for line in curr:
        line.append(thing)
        line.insert(0, thing)

    curr.insert(0, [thing] * len(curr[-1]))
    curr.append([thing] * len(curr[0]))

    new = [['.']*len(curr[0]) for x in range(len(curr))]

    for i in range(len(curr)):
        for j in range(len(curr)):
            if step % 2 == 0:
                new[i][j] = getVal(curr, i, j, algo)
            else:
                new[i][j] = getVal2(curr, i, j, algo)
    curr = new

ans = 0

for i in range(len(curr)):
    for j in range(len(curr[0])):
        if curr[i][j] == '#':
            ans += 1

print(ans)  # answer is 16389
