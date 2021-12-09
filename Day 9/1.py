input = open('Day 9/input')
temp = input.read()
arr = [[int(i) for i in ar] for ar in [list(c) for c in temp.split('\n')]]


def risk_level(arr, i, j):
    curr = arr[i][j]

    if i >= 1 and curr >= arr[i-1][j]:
        return 0
    if i < len(arr)-1 and curr >= arr[i+1][j]:
        return 0
    if j >= 1 and curr >= arr[i][j - 1]:
        return 0
    if j < len(arr[0])-1 and curr >= arr[i][j+1]:
        return 0

    return curr + 1


ans = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        ans += risk_level(arr, i, j)

print(ans)  # answer is 518
