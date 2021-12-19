fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0

with open(fname) as f:
    data = map(lambda x: x, f.readlines())

conns = []

for l in data:
    p1, p2 = l.split(" -> ")
    conns.append( ([int(x) for x in p1.split(',')], [int(x) for x in p2.split(',')]) )

count = Counter()

for p1,p2 in conns:
    if p1[0] == p2[0]:
        y1 = min(p1[1], p2[1])
        y2 = max(p1[1], p2[1])
        for y in range(y1, y2 + 1):
            p = (p1[0],y)
            count[p] += 1

    elif p1[1] == p2[1]:
        x1 = min(p1[0], p2[0])
        x2 = max(p1[0], p2[0])
        for x in range(x1, x2 + 1):
            p = (x, p1[1])
            count[p] += 1
    elif abs(p1[0] - p2[0]) == abs(p1[1] - p2[1]):
        stepx = 1 if p2[0] > p1[0] else -1
        stepy = 1 if p2[1] > p1[1] else -1
        steps = abs(p2[0] - p1[0])
        p = (p1[0], p1[1])
        for i in range(0, steps + 1):
            count[p] += 1
            cx, cy = p
            p = (cx + stepx, cy + stepy)

#print(count)

result = 0
for p in count:
    if count[p] > 1:
        result += 1

print(result)
pyperclip.copy(result)