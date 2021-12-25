fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

cuc = []
for l in data:
    cuc.append([x for x in l ])

#> then v
iter = 0
while True:
    iter += 1
    moved = False
    new_cuc = []
    for i,y in enumerate(cuc):
        new_cuc.append([ dd for dd in cuc[i] ])

    MAXX = len(cuc[0])
    MAXY = len(cuc)
    tomove = []
    for y in range(len(cuc)):
        for x in range(len(cuc[0])):
            if cuc[y][x] == ">":
                if (x == MAXX - 1):
                    if cuc[y][0] == '.':
                        tomove.append(((x,y), (0,y)))
                elif new_cuc[y][x+1] == ".":
                    tomove.append(((x,y), (x+1,y)))

    for pold, pnew in tomove:
        new_cuc[pold[1]][pold[0]] = "."
        new_cuc[pnew[1]][pnew[0]] = ">"
        moved = True

    cuc = new_cuc
    tomove = []

    for y in range(len(cuc)):
        for x in range(len(cuc[0])):
            if cuc[y][x] == "v":
                if (y == MAXY - 1):
                    if cuc[0][x] == '.':
                        tomove.append(((x,y), (x,0)))
                elif new_cuc[y+1][x] == ".":
                    tomove.append(((x,y), (x,y+1)))

    for pold, pnew in tomove:
        new_cuc[pold[1]][pold[0]] = "."
        new_cuc[pnew[1]][pnew[0]] = "v"
        moved = True

    if not moved:
        result = iter
        break

    cuc = new_cuc

    #print(iter)
    #for y in range(len(cuc)):
    #    for x in range(len(cuc[0])):
    #        print(new_cuc[y][x], end='')
    #    print()
    #print()

print(result)
pyperclip.copy(result)
print(0) # for check.py