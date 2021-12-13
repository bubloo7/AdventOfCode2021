input = open('Day 13/input')

arr = input.read().split('\n')
cords = []
folds = []

maxx = -1
maxy = -1
minx = 99999
miny = 99999

for line in arr:
    if ',' in line:
        split = line.split(',')
        cords.append((int(split[0]), int(split[1])))
        maxx = max(maxx, int(split[0]) + 1)
        maxy = max(maxy, int(split[1]) + 1)
    elif '=' in line:
        split = line.split('=')
        folds.append((split[0][-1], int(split[1])))
        if split[0][-1] == 'x':
            minx = min(minx, int(split[1]))
        else:
            miny = min(miny, int(split[1]))


paper = [['.']*(maxx) for i in range(maxy)]

for x, y in cords:
    paper[y][x] = '*'


for f, num in folds:
    if f == 'x':
        for i in range(maxy):
            for j in range(num, maxx):
                if paper[i][j] == '*':
                    paper[i][2*num - j] = '*'
                    paper[i][j] = '.'
    else:
        for i in range(num, maxy):
            for j in range(maxx):
                if paper[i][j] == '*':
                    paper[2*num - i][j] = '*'
                    paper[i][j] = '.'


for i in range(miny):
    for j in range(minx):
        print(paper[i][j] + ' ', end='')
    print()

# answer is CJHAZHKU
