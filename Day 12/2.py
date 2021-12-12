import copy
input = open('Day 12/input').read().split('\n')

edgeList = {}
for i in input:
    v = i.split('-')
    curr1 = edgeList.get(v[0], [])
    curr2 = edgeList.get(v[1], [])
    curr1.append(v[1])
    curr2.append(v[0])
    edgeList[v[0]] = curr1
    edgeList[v[1]] = curr2

ans = 0

q = [('start', {}, False)]

while len(q) != 0:
    curr, visited, dbl = q.pop()
    if curr == 'end':
        ans += 1
        continue

    for v in edgeList[curr]:
        if v == 'start':
            continue
        if v.isupper():
            if visited.get(v, 0) < len(edgeList[v]):
                dc = copy.deepcopy(visited)
                dc[v] = visited.get(v, 0) + 1
                q.append((v, dc, dbl))
        else:
            if visited.get(v, 0) < 1:
                dc = copy.deepcopy(visited)
                dc[v] = 1
                q.append((v, dc, dbl))

            elif not dbl:
                dc = copy.deepcopy(visited)
                dc[v] = 2
                q.append((v, dc, True))

print(ans)  # answer is 144603
