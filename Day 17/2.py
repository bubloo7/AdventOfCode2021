ans = 0
for x in range(1, 200):
    for y in range(-115, 1000):
        for step in range(1000):

            opp = x - step - 1
            xcord = x*(x+1)/2 - opp*(opp+1)/2
            if step + 1 >= x:
                xcord = x*(x+1)/2
            opp = y - step - 1
            ycord = y*(y+1)/2 - opp*(opp+1)/2

            if xcord > 199 or ycord < -114:
                break

            if xcord >= 153 and xcord <= 199 and ycord >= -114 and ycord <= -75:
                ans += 1
                break

print(ans)  # answer is 3186
