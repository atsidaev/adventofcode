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

            
print(result)
pyperclip.copy(result)