# This was my inital attempt at solving the problem which unfortunately didn't work.
# This was the hardest problem yet and I struggled a lot with it initially until I realized we could use trees to represent the data.
# I thought it would still be fun to leave it up here though just to see how much clearer my current solution was.
# It's also kinda funny how much I overcomplicated the problem lol.

import json
from typing import Iterable


# based on: https://stackoverflow.com/a/6039138/13951395
def depth(L): return isinstance(L, list) and max(map(depth, L))+1


def alll(l, c):
    if type(l) == int:
        return c
    else:
        for e in l:
            c.append(e)
            r = alll(e, [])
            for e2 in r:
                c.append(e2)

        return c


def magnitude(num):
    if type(num) == list:
        return magnitude(num[0])*3 + magnitude(num[1])*2
    else:
        return num


def explode(num):
    stack = []
    all = []
    d4 = []
    deepest = []
    explo = None

    for elem in num:
        all.append(elem)
        stack.append(elem)

    while len(stack) != 0:
        curr = stack.pop()

        if type(curr) == int:
            continue

        if depth(curr) == 4:
            d4.append(curr)
        for elem in curr:
            stack.append(elem)
            all.append(elem)

    for d5 in d4:
        for eeelem in d5:
            # print(eeelem, depth(eeelem))
            if depth(eeelem) == 3:
                for eeeelem in eeelem:
                    if depth(eeeelem) == 2:
                        for eeeeelem in eeeelem:
                            if depth(eeeeelem) == 1:
                                deepest.append(eeeeelem)

    flag1 = False
    # print(deepest)
    all = alll(num, [])

    for thingy in all:
        if type(thingy) == int:
            continue
        if flag1:
            break
        for i in range(len(deepest)):
            thing = deepest[i]
            if thing is thingy:
                explo = thing
                flag1 = True
                break

    # print('explo', explo)
    filter = [num]
    oppfilter = []

    for elem in all:
        if type(elem) == list:
            filter.append(elem)
        else:
            oppfilter.append(elem)

    # for iii in range(len(filter)):
    #     print(iii, filter[iii])
    # # print(oppfilter)

    for ind in range(len(filter)):

        if filter[ind] is explo:
            outer = filter[ind-1]

            # [[explo], something]
            if outer[0] is explo:
                # handles right
                ll = outer[1]

                if type(ll) == int:
                    outer[1] += explo[1]
                else:
                    while type(ll[0]) != int:
                        ll = ll[0]
                    ll[0] += explo[1]

                # handle left pls
                ind2 = ind-2
                while ind2 >= 0 and type(filter[ind2][0]) != int:
                    ind2 -= 1
                    print('bro pls', filter[ind2])

                if ind2 >= 0:
                    filter[ind2][0] += explo[0]
        # [something, [explo]]
            else:
                print('check1')
                outer = filter[ind-1]

                # handles left
                ll = outer[0]
                if type(ll) == int:
                    outer[0] += explo[0]
                else:
                    while type(ll[1]) != int:
                        ll = ll[1]
                    ll[1] += explo[0]

                # handle right pls
                ind3 = ind-2
                old = outer
                while ind3 >= 0 and filter[ind3][1] is old:
                    old = filter[ind3]
                    ind3 -= 1

                    print('bro pls2', filter[ind3])

                old = filter[ind3]
                if ind3 >= 0:
                    if type(old[1]) == int:
                        print('check2', ind3)

                        old[1] += explo[1]

                    else:
                        cump = old[1]
                        while type(cump[0]) != int:
                            cump = cump[0]

                        cump[0] += explo[1]

                    # print('old is', old, ind3)

        # print('e',all[ind])

    flag2 = False
    newt = None
    for thingy in all:
        if type(thingy) == int:
            continue
        if flag2:
            break
        for aa in range(len(thingy)):
            if thingy[aa] is explo:
                thingy[aa] = 0
                newt = thingy
                print('rm', explo)
                flag2 = True
                break


arr = [json.loads(x) for x in open('Day 18/input').read().split('\n')]

sum = [arr[0], arr[1]]
sum = [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
print(sum)

explode(sum)

print(sum)

# all = all(sum, [])
