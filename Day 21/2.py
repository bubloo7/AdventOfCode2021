pos1, pos2 = [int(line[-1])
              for line in open('Day 21/input').read().split('\n')]

wins1, wins2 = 0, 0

q = [(True, pos1, 0, pos2, 0)]
hmap = {q[0]: 1}

count = 0
while len(q) != 0:
    curr = q.pop(0)
    player1Turn, pos1, points1, pos2, points2 = curr
    num = hmap[curr]
    del hmap[curr]
    if player1Turn:

        tempPoints = pos1 + 3 if pos1 + 3 < 11 else (pos1 + 3) % 10
        if tempPoints + points1 > 20:
            wins1 += num*1
        else:
            newT = (not player1Turn, tempPoints,
                    points1 + tempPoints, pos2, points2)
            if newT in hmap:
                hmap[newT] += num*1
            else:
                q.append(newT)
                hmap[newT] = num*1

        tempPoints = pos1 + 4 if pos1 + 4 < 11 else (pos1 + 4) % 10
        if tempPoints + points1 > 20:
            wins1 += num*3
        else:
            newT = (not player1Turn, tempPoints,
                    points1 + tempPoints, pos2, points2)
            if newT in hmap:
                hmap[newT] += num*3
            else:
                q.append(newT)
                hmap[newT] = num*3

        tempPoints = pos1 + 5 if pos1 + 5 < 11 else (pos1 + 5) % 10
        if tempPoints + points1 > 20:
            wins1 += num*6
        else:
            newT = (not player1Turn, tempPoints,
                    points1 + tempPoints, pos2, points2)
            if newT in hmap:
                hmap[newT] += num*6
            else:
                q.append(newT)
                hmap[newT] = num*6

        tempPoints = pos1 + 6 if pos1 + 6 < 11 else (pos1 + 6) % 10
        if tempPoints + points1 > 20:
            wins1 += num*7
        else:
            newT = (not player1Turn, tempPoints,
                    points1 + tempPoints, pos2, points2)
            if newT in hmap:
                hmap[newT] += num*7
            else:
                q.append(newT)
                hmap[newT] = num*7

        tempPoints = pos1 + 7 if pos1 + 7 < 11 else (pos1 + 7) % 10
        if tempPoints + points1 > 20:
            wins1 += num*6
        else:
            newT = (not player1Turn, tempPoints,
                    points1 + tempPoints, pos2, points2)
            if newT in hmap:
                hmap[newT] += num*6
            else:
                q.append(newT)
                hmap[newT] = num*6

        tempPoints = pos1 + 8 if pos1 + 8 < 11 else (pos1 + 8) % 10
        if tempPoints + points1 > 20:
            wins1 += num*3
        else:
            newT = (not player1Turn, tempPoints,
                    points1 + tempPoints, pos2, points2)
            if newT in hmap:
                hmap[newT] += num*3
            else:
                q.append(newT)
                hmap[newT] = num*3

        tempPoints = pos1 + 9 if pos1 + 9 < 11 else (pos1 + 9) % 10
        if tempPoints + points1 > 20:
            wins1 += num*1
        else:
            newT = (not player1Turn, tempPoints,
                    points1 + tempPoints, pos2, points2)
            if newT in hmap:
                hmap[newT] += num*1
            else:
                q.append(newT)
                hmap[newT] = num*1
    else:

        tempPoints = pos2 + 3 if pos2 + 3 < 11 else (pos2 + 3) % 10
        if tempPoints + points2 > 20:
            wins2 += num*1
        else:
            newT = (not player1Turn, pos1, points1,
                    tempPoints, points2 + tempPoints)
            if newT in hmap:
                hmap[newT] += num*1
            else:
                q.append(newT)
                hmap[newT] = num*1

        tempPoints = pos2 + 4 if pos2 + 4 < 11 else (pos2 + 4) % 10
        if tempPoints + points2 > 20:
            wins2 += num*3
        else:
            newT = (not player1Turn, pos1, points1,
                    tempPoints, points2 + tempPoints)
            if newT in hmap:
                hmap[newT] += num*3
            else:
                q.append(newT)
                hmap[newT] = num*3

        tempPoints = pos2 + 5 if pos2 + 5 < 11 else (pos2 + 5) % 10
        if tempPoints + points2 > 20:
            wins2 += num*6
        else:
            newT = (not player1Turn, pos1, points1,
                    tempPoints, points2 + tempPoints)
            if newT in hmap:
                hmap[newT] += num*6
            else:
                q.append(newT)
                hmap[newT] = num*6

        tempPoints = pos2 + 6 if pos2 + 6 < 11 else (pos2 + 6) % 10
        if tempPoints + points2 > 20:
            wins2 += num*7
        else:
            newT = (not player1Turn, pos1, points1,
                    tempPoints, points2 + tempPoints)
            if newT in hmap:
                hmap[newT] += num*7
            else:
                q.append(newT)
                hmap[newT] = num*7

        tempPoints = pos2 + 7 if pos2 + 7 < 11 else (pos2 + 7) % 10
        if tempPoints + points2 > 20:
            wins2 += num*6
        else:
            newT = (not player1Turn, pos1, points1,
                    tempPoints, points2 + tempPoints)
            if newT in hmap:
                hmap[newT] += num*6
            else:
                q.append(newT)
                hmap[newT] = num*6

        tempPoints = pos2 + 8 if pos2 + 8 < 11 else (pos2 + 8) % 10
        if tempPoints + points2 > 20:
            wins2 += num*3
        else:
            newT = (not player1Turn, pos1, points1,
                    tempPoints, points2 + tempPoints)
            if newT in hmap:
                hmap[newT] += num*3
            else:
                q.append(newT)
                hmap[newT] = num*3

        tempPoints = pos2 + 9 if pos2 + 9 < 11 else (pos2 + 9) % 10
        if tempPoints + points2 > 20:
            wins2 += num*1
        else:
            newT = (not player1Turn, pos1, points1,
                    tempPoints, points2 + tempPoints)
            if newT in hmap:
                hmap[newT] += num*1
            else:
                q.append(newT)
                hmap[newT] = num*1

print(max(wins1, wins2))  # answer is 133029050096658
