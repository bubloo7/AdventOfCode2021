arr = open('Day 14/input').read().split('\n')

string = arr[0]

rules = {}
for i in range(2, len(arr)):
    curr = arr[i].split(' -> ')
    rules[curr[0]] = curr[0][0] + curr[1]

for i in range(10):
    newStr = ''
    for i in range(len(string)-1):
        curr = string[i:i+2]
        newStr += rules.get(curr, curr[0])

    string = newStr + string[-1]

counts = {}
for c in string:
    counts[c] = counts.get(c, 0) + 1

print(max(counts.values()) - min(counts.values())) # answer is 2967
