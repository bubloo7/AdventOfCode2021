input = open("Day 10/input")
arr = input.read().split('\n')

matching = { ')' : '(', '}' : '{' , ']': '[', '>': '<'}
score = { '(' : 1, '[' : 2 , '{': 3, '<': 4}

incompleteLines = []
for line in arr:
    stack = []
    incomplete = True
    for c in line:
        if c in matching:
            if stack.pop() != matching[c]:
                incomplete = False
                break
        else:
            stack.append(c)
    
    if incomplete:
        incompleteLines.append(stack)

ans = []
for i in range(len(incompleteLines)):
    points = 0
    currStack = incompleteLines[i]
    while len(currStack) != 0:
        elem = currStack.pop()
        points *= 5
        points += score[elem]
    ans.append(points)


print(sorted(ans)[int(len(ans)/2)])
