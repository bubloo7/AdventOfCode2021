import heapq
arr = [[int(i) for i in ar] for ar in [list(c)for c in open("Day 15/input").read().split('\n')]]

n = len(arr)
[arr[c].append(0) for c in range(len(arr)) for d in range(n*4)]
[arr.append([0] * (5*n)) for i in range(n*4)]


for i in range(n ):
    for j in range(n, n*5):
        arr[i][j] = max((arr[i][j-n] + 1)%10,1)

for i in range(n, n*5):
    for j in range(n*5):
        arr[i][j] = max((arr[i-n][j] + 1)%10,1)

pq = []

visited = [[False]*n*5 for i in range(n*5)]
heapq.heappush(pq, (0, (0, 0)))
ans = -1  
while True:

    weight, cords = heapq.heappop(pq)
    x, y = cords
    if x == len(arr) - 1 and y == len(arr[0]) - 1:
        ans = weight + arr[x][y] - arr[0][0]
        break

    if visited[x][y]:
        continue

    visited[x][y] = True

    if x < len(arr) - 1 and not visited[x+1][y]:
        heapq.heappush(pq, (weight + arr[x][y], (x+1, y)))
    if x > 0 and not visited[x-1][y]:
        heapq.heappush(pq, (weight + arr[x][y], (x-1, y)))
    if y < len(arr) - 1 and not visited[x][y+1]:
        heapq.heappush(pq, (weight + arr[x][y], (x, y+1)))
    if y > 0 and not visited[x][y-1]:
        heapq.heappush(pq, (weight + arr[x][y], (x, y-1)))


print(ans)  # answer is 824
