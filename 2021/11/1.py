fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

omap = []

for l in data:
    m = [];
    omap.append(m)
    for c in l:
        m.append(int(c))


for r in range(100):
    for y in range(len(omap)):
        for x in range(len(omap[0])):
            omap[y][x] += 1

    visited = []
    while True:
        found9 = False
        for y in range(len(omap)):
            for x in range(len(omap[0])):
                if omap[y][x] > 9 and not (x,y) in visited:
                    visited.append((x,y))
                    found9 = True
                    adj = [ (x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1),(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1) ]
                    for ax,ay in adj:
                        if ax >= 0 and ay >=0 and ay < len(omap) and ax < len(omap[0]):
                            omap[ay][ax] += 1
          #                  print("i", (x,y), (ax,ay), omap)

        if not found9:
            for y in range(len(omap)):
                for x in range(len(omap[0])):
                    if omap[y][x] > 9:
                        omap[y][x] = 0
            break

    result += len(visited)
    #print(omap)     

print(result)
pyperclip.copy(result)