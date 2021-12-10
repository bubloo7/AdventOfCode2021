input = open("Day 10/input")
arr = input.read().split('\n')

matching = { ')' : '(', '}' : '{' , ']': '[', '>': '<'}
score = { ')' : 3, ']' : 57 , '}': 1197, '>': 25137}

ans = 0
for line in arr:
    stack = []
    for c in line:
        if c in matching:
            if stack.pop() != matching[c]:
                ans += score[c]         
                break
        else:
            stack.append(c)

print(ans) # answer is 374061
