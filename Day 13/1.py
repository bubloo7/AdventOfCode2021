input = open('Day 13/input')

arr = input.read().split('\n')
cords = []
folds = []

maxx = -1
maxy = -1

for line in arr:
    if ',' in line:
        split = line.split(',')
        cords.append((int(split[0]), int(split[1])))
        maxx = max(maxx, int(split[0]) + 1)
        maxy = max(maxy, int(split[1]) + 1)
    elif '=' in line:
        split = line.split('=')
        folds.append((split[0][-1], int(split[1])))

paper = [[0]*(maxx) for i in range(maxy)]

for x, y in cords:
    paper[y][x] = 1

for f, num in folds:
    if f == 'x':
        for i in range(maxy):
            for j in range(num, maxx):
                if paper[i][j] == 1:
                    paper[i][2*num - j] = 1
                    paper[i][j] = 0
    else:
        for i in range(num, maxy):
            for j in range(maxx):

                if paper[i][j] == 1:
                    paper[2*num - i][j] = 1
                    paper[i][j] = 0

    break

ans = sum(sum(paper, []))


print(ans)  # answer is 666
