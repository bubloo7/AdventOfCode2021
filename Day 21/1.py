pos1, pos2 = [int(line[-1])
              for line in open('Day 21/input').read().split('\n')]

score1, score2 = 0, 0
curr = 1
roles = 0

while(score1 < 1000 and score2 < 1000):
    if roles % 2 == 0:
        pos1 += curr
        curr = (curr + 1) % 10
        pos1 += curr
        curr = (curr + 1) % 10
        pos1 += curr
        curr = (curr + 1) % 10
        pos1 = pos1 if pos1 < 11 else pos1 % 10
        score1 += pos1
    else:
        pos2 += curr
        curr = (curr + 1) % 10
        pos2 += curr
        curr = (curr + 1) % 10
        pos2 += curr
        curr = (curr + 1) % 10
        pos2 = pos2 if pos2 < 11 else pos2 % 10
        score2 += pos2
    roles += 3

print(roles*min(score1, score2))  # answer is 805932
