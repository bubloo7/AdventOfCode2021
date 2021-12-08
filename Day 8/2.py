input = open("Day 8/input")

arr = input.read().split("\n")

pval = {
    "a": 3,
    "b": 5,
    "c": 7,
    "d": 11,
    "e": 13,
    "f": 17,
    "g": 19
}

ans = 0
for i in arr:
    curr = i.split(' ')
    currv = [1, 1, 1, 1, 1, 1, 1, 1, 4849845, 1]
    len5 = []
    len6 = []
    for j in range(10):
        s = curr[j]
        if len(s) == 2:
            for c in s:
                currv[1] *= pval[c]
        elif len(s) == 3:
            for c in s:
                currv[7] *= pval[c]
        elif len(s) == 4:
            for c in s:
                currv[4] *= pval[c]
        elif len(s) == 5:
            temp = 1
            for c in s:
                temp *= pval[c]
            len5.append(temp)
        elif len(s) == 6:
            temp = 1
            for c in s:
                temp *= pval[c]
            len6.append(temp)

    for k in len6:
        if k % currv[4] == 0:
            currv[9] = k
        elif k % currv[1] == 0:
            currv[0] = k
        else:
            currv[6] = k

    for k in len5:
        if k % currv[1] == 0:
            currv[3] = k
        elif currv[6] % k == 0:
            currv[5] = k
        else:
            currv[2] = k

    hmap = {}

    aaa = 0
    for v in currv:
        hmap[v] = aaa
        aaa += 1

    temppp = 0
    for j in range(11, 15):
        temppp *= 10
        s = curr[j]
        temp = 1
        for c in s:
            temp *= pval[c]
        temppp += hmap[temp]
    ans += temppp

print(ans)  # answer is 933305
