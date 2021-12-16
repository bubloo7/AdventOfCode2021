def evaluate(type, nums):
    if type == 0:
        return sum(nums)
    elif type == 1:
        ans = 1
        for num in nums:
            ans *= num
        return ans
    elif type == 2:
        return min(nums)
    elif type == 3:
        return max(nums)

    elif type == 5:
        return 1 if nums[0] > nums[1] else 0
    elif type == 6:
        return 1 if nums[0] < nums[1] else 0
    elif type == 7:
        return 1 if nums[0] == nums[1] else 0


def header(binary, i):

    version = int(binary[i:i+3], 2)
    type = int(binary[i+3:i+6], 2)
    return (version, type, i + 6)


def literal_val(binary, i):
    lvalues = []
    cont = True
    while cont:
        cont = binary[i] == '1'
        lvalues.append(binary[i+1:i+5])
        i += 5

    a = ''
    for aa in lvalues:
        a += aa
    return (i, int(a, 2))


def id0(binary, i, type):
    numbits = int(binary[i:i+15], 2)
    i += 15
    j = i
    arrr = []
    while j != i + numbits:
        version, type2, j = header(binary, j)

        if type2 == 4:
            j, b = literal_val(binary, j)
            arrr.append(b)

        elif binary[j] == '0':
            j += 1
            j, b = id0(binary, j, type2)
            arrr.append(b)

        else:
            j += 1
            j, b = id1(binary, j, type2)
            arrr.append(b)

    return (j, evaluate(type, arrr))


def id1(binary, i, type):
    numps = int(binary[i:i+11], 2)
    i += 11
    j = i
    counter = 0
    arrr = []
    while counter < numps:
        version, type2, j = header(binary, j)
        if type2 == 4:
            j, b = literal_val(binary, j)
            arrr.append(b)

        elif binary[j] == '0':
            j += 1
            j, b = id0(binary, j, type2)
            arrr.append(b)
        else:
            j += 1
            j, b = id1(binary, j, type2)
            arrr.append(b)
        counter += 1
    return (j, evaluate(type, arrr))


binary = (len(open('Day 16/input').read())*4 - len(bin(int(open('Day 16/input').read(), 16))
          [2:]))*'0' + bin(int(open('Day 16/input').read(), 16))[2:]

i = 0
ans = -1
while i < len(binary):
    if int(binary[i:], 2) == 0:
        break
    version, type, i = header(binary, i)
    if type == 4:
        i, ans = literal_val(binary, i)
    elif binary[i] == '0':
        i, ans = id0(binary, i+1, type)

    else:
        i, ans = id1(binary, i+1, type)

print(ans)  # answer is 13476220616073
