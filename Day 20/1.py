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


algo = input[0]

curr = []
for i in range(2, len(input)):
    curr.append(list(input[i]))


for step in range(2):
    thing = '.' if step % 2 == 0 else '#'
    for line in curr:
        line.append(thing)
        line.insert(0, thing)

        line.append(thing)
        line.insert(0, thing)

        line.append(thing)
        line.insert(0, thing)

        line.append(thing)
        line.insert(0, thing)

        line.append(thing)
        line.insert(0, thing)

    curr.insert(0, [thing] * len(curr[-1]))
    curr.append([thing] * len(curr[0]))

    curr.insert(0, [thing] * len(curr[-1]))
    curr.append([thing] * len(curr[0]))

    curr.insert(0, [thing] * len(curr[-1]))
    curr.append([thing] * len(curr[0]))

    curr.insert(0, [thing] * len(curr[-1]))
    curr.append([thing] * len(curr[0]))

    curr.insert(0, [thing] * len(curr[-1]))
    curr.append([thing] * len(curr[0]))

    new = [['.']*len(curr[0]) for x in range(len(curr))]

    for i in range(len(curr)):
        for j in range(len(curr)):

            new[i][j] = getVal(curr, i, j, algo)

    curr = new

ans = 0

for i in range(1, len(curr)-1):
    for j in range(1, len(curr[0])-1):
        if curr[i][j] == '#':
            ans += 1

print(ans)  # answer is 4917
