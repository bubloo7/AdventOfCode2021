# This problem was interesting and I kinda overdid it tbh. Runtime doesn't matter for AoC but I wanted to optimize the code anyway haha. Be sure to look at board.py to see how I solved this problem!
from board import board

input = open("Day 4/input")

arr0 = input.read().split('\n')

bingo = arr0[0].split(',')

for i in range(len(bingo)):
    bingo[i] = int(bingo[i])

boards = []
curr = []
for i in range(2, len(arr0)):
    if arr0[i]=='':
        boards.append(board(curr))
        curr = []
        continue
    temp =  arr0[i].split(' ')
    temp2 = [0, 0, 0, 0, 0]
    h = 0
    for j in range(len(temp)):
        if temp[j] == " " or temp[j] == "":
            continue
        temp2[h] = int(temp[j])
        h += 1
     
    if h != 5:
        breaks = 5/0
    curr.append(temp2)

boards.append(board(curr))


def easy(bingo, boards):
    for ind in range(len(bingo)):
        i = bingo[ind]
        for j in range(len(boards)):
            boa = boards[j]
            boa.num(i)
            if boa.bingo():
                print("board", j)
                print(boa)
                return sum(boa.nums.keys()) * i



ans = easy(bingo, boards)

print("Answer:",ans) # answer is 50008

