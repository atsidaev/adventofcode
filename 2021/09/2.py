fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x, f.readlines()))

data = [ [ int(c) for c in x.strip() ] for x in data ]

mins = []

for y in range(len(data)):
    for x in range(len(data[y])):
        ismin = True
        if y != len(data) - 1 and data[y][x] >= data[y + 1][x]:
            ismin = False
        if y != 0 and data[y][x] >= data[y - 1][x]:
            ismin = False
        if x != len(data[0]) - 1 and data[y][x] >= data[y][x + 1]:
            ismin = False
        if x != 0 and data[y][x] >= data[y][x - 1]:
            ismin = False

        if ismin:
        #    print(x,y, data[y][x])
            result += data[y][x] + 1
            mins.append((x,y))

basins = []

for minp in mins:
    basin = set([ minp ])
    visited = set([])
    queue = [ minp ]
    while queue:
        x,y = queue.pop(0)
        
        for ax, ay in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
            p = (ax, ay)
            if ay < len(data) and ax < len(data[0]) and ay >= 0 and ax >= 0 and not p in visited and data[ay][ax] != 9:
                queue.append(p)
                visited.add(p)
                basin.add(p)
  
    if len(basin) > 1 and not basin in basins:
        basins.append(basin)

#for b in basins:
#    print("Basin length: ", len(b))
#    for d in range(len(data)):
#        for k in range(len(data[d])):
#            if (k,d) in b:
#                print('\033[96m', end = "")
#            print(data[d][k], end = '')
#            if (k,d) in b:
#                print('\033[0m', end="")
#        print("")
#    print()

print(basins)
basins = sorted([ len(x) for x in basins ])
print("s", basins)

result = 1
for s in sorted(basins)[-3:]:
    result *= s

print(result)
pyperclip.copy(result)
