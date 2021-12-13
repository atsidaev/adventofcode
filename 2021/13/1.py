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

rrr = set([])
for x,y in sheet:
    x = int(x)
    y = int(y)
    if x == 655:
        continue
    elif x < 655:
        rrr.add((x,y))
    else:
        rrr.add((655 - (x - 655), y))

result = len(rrr)
print(result)
pyperclip.copy(result)