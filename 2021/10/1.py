fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

pairs = { '{': '}', '(': ')', '[': ']' , '<': '>' }

for line in data:
    stack = []
    count = 0
    for c in line:
        if c in [ '{', '(', '[', '<' ]:
            stack.append(c)
        elif c in [ '}', ')', ']', '>' ]:
            m = stack.pop()
            if pairs[m] != c:
                print(c)
                if c == ')':
                    result += 3
                    break
                elif c == ']':
                    result += 57
                    break
                elif c == '}':
                    result += 1197
                    break
                elif c == '>':
                    result += 25137
                    break
        else:
            print(c)
        

#        count += 1

print(result)
pyperclip.copy(result)