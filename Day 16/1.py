global ans
ans = 0


def header(binary, i):
    global ans

    version = int(binary[i:i+3], 2)
    type = int(binary[i+3:i+6], 2)
    ans += version
    return (version, type, i + 6)


def literal_val(binary, i):
    lvalues = []
    cont = True
    while cont:
        cont = binary[i] == '1'
        lvalues.append(int(binary[i+1:i+5]))
        i += 5
    return (i, lvalues)


def id0(binary, i):
    numbits = int(binary[i:i+15], 2)
    i += 15
    j = i
    while j != i + numbits:
        version, type, j = header(binary, j)

        if type == 4:
            j, lvalues = literal_val(binary, j)
        elif binary[j] == '0':
            j += 1
            j = id0(binary, j)
        else:
            j += 1
            j = id1(binary, j)

    return j


def id1(binary, i):
    numps = int(binary[i:i+11], 2)
    i += 11
    j = i
    counter = 0
    while counter < numps:
        version, type, j = header(binary, j)
        if type == 4:
            j, lvalues = literal_val(binary, j)
        elif binary[j] == '0':
            j += 1
            j = id0(binary, j)
        else:
            j += 1
            j = id1(binary, j)
        counter += 1
    return j


binary = (len(open('Day 16/input').read())*4 - len(bin(int(open('Day 16/input').read(), 16))
          [2:]))*'0' + bin(int(open('Day 16/input').read(), 16))[2:]

i = 0
while i < len(binary):
    if int(binary[i:], 2) == 0:
        break
    version, type, i = header(binary, i)
    if type == 4:
        i, lvalues = literal_val(binary, i)
    elif binary[i] == '0':
        i = id0(binary, i+1)
    else:
        i = id1(binary, i+1)


print(ans)  # answer is 940
