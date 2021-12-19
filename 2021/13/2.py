fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

sheet = []
instructions = []
with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

instr = False
for d in data:
    if not instr and d != '':
        x,y = d.split(",")
        sheet.append((x,y))
    elif not instr and d == "":
        instr = True
    else:
        instructions.append(d)

print(instructions, len(sheet))

def foldx(v):
    rrr = set([])
    for x,y in sheet:
        x = int(x)
        y = int(y)
        if x == v:
            continue
        elif x <= v:
            rrr.add((x,y))
        else:
            rrr.add((v - (x - v), y))
    return list(rrr)


def foldy(v):
    rrr = set([])
    for x,y in sheet:
        x = int(x)
        y = int(y)
        if y == v:
            continue
        elif y < v:
            rrr.add((x,y))
        else:
            rrr.add((x, v - (y - v)))
    return list(rrr)

for i in instructions:
    a,b,c = i.split(" ")
    d,v = c.split("=")
    v = int(v)
    if d == "x":
        sheet = foldx(v)
    elif d == "y":
        sheet = foldy(v)
    else:
        raise "123"

maxx = max([x for x,y in sheet])
maxy = max([y for x,y in sheet])
for y in range(maxy+1):
    for x in range(maxx+1):
        if (x,y) in sheet:
            print("Ж", end = '')
        else:
            print(" ", end = "")
    print()

result = "EPUELPBR" # hack for answer checker
print(result)
pyperclip.copy(result)