arr = open('Day 14/input').read().split('\n')

string = {}

for i in range(len(arr[0]) - 1):
    string[arr[0][i:i+2]] = string.get(arr[0][i:i+2], 0) + 1

rules = {}
for i in range(2, len(arr)):
    curr = arr[i].split(' -> ')
    rules[curr[0]] = curr[1]

for i in range(40):
    newString = {}
    for pair in string:
        if pair in rules.keys():
            newString[pair[0] + rules[pair]
                      ] = newString.get(pair[0] + rules[pair], 0) + string[pair]
            newString[rules[pair] + pair[1]
                      ] = newString.get(rules[pair] + pair[1], 0) + string[pair]

        else:
            newString[pair] = newString.get(pair, 0) + string[pair]

    string = newString

counts = {}

for k in string:
    counts[k[0]] = counts.get(k[0], 0) + string[k]
    counts[k[1]] = counts.get(k[1], 0) + string[k]

counts[arr[0][0]] += 1
counts[arr[0][-1]] += 1

print((max(counts.values()) - min(counts.values()))//2) # answer is 3692219987038
