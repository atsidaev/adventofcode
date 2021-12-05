fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = map(lambda x: x, f.readlines())

conns = []

for l in data:
    p1, p2 = l.split(" -> ")
    conns.append( ([int(x) for x in p1.split(',')], [int(x) for x in p2.split(',')]) )

conns = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], conns))

count = {}

for p1,p2 in conns:
    if p1[0] == p2[0]:
        y1 = min(p1[1], p2[1])
        y2 = max(p1[1], p2[1])
        for y in range(y1, y2 + 1):
            p = (p1[0],y)
  #          print(p1, p2, p)
            if not p in count:
                count[p] = 0
#            else:
 #               print(p, count[p])
            count[p] += 1

    elif p1[1] == p2[1]:
        x1 = min(p1[0], p2[0])
        x2 = max(p1[0], p2[0])
        for x in range(x1, x2 + 1):
            p = (x, p1[1])
 #           print(p1, p2, p)
            if not p in count:
                count[p] = 0
            count[p] += 1

print(count)

result = 0
for p in count:
    if count[p] > 1:
        result += 1

print(result)
pyperclip.copy(result)