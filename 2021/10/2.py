fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result1 = 0
result2 = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

pairs = { '{': '}', '(': ')', '[': ']' , '<': '>' }
score = { ')': 1, ']': 2, '}': 3 , '>': 4 }

pts_all = []

for line in data:
    stack = []
    count = 0
    bad = False
    for c in line:
        if c in pairs.keys():
            stack.append(c)
        elif c in pairs.values():
            m = stack.pop()
            if pairs[m] != c:
                # print(count, m, c, stack, result)
                if c == ')':
                    result1 += 3
                    bad = True
                    break
                elif c == ']':
                    result1 += 57
                    bad = True
                    break
                elif c == '}':
                    result1 += 1197
                    bad = True
                    break
                elif c == '>':
                    result1 += 25137
                    bad = True
                    break
        else:
            print(c)
            raise "123123"

        count += 1
    if bad:
        print(count, line, stack)
    else:
        pts = 0
        while stack:
            m = stack.pop()
            p = pairs[m]
            pts *= 5
            pts += score[p]
        print(line, pts)
        pts_all.append(pts)

pts_all = sorted(pts_all)
print(pts_all, pts_all[int(len(pts_all) / 2)])
print(result1, result2)
pyperclip.copy(result2)