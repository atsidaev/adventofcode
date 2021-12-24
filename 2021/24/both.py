fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

prog = data

def run(inp):
    regs = {
        'x': 0,
        'y': 0,
        'z': 0,
        'w': 0
    }

    pos = 0
    zs = []
    for l in prog:
        parts = l.split()
    # print(parts)
        if parts[0] == "inp":
            regs[parts[1]] = int(inp[pos])
            pos += 1
        elif parts[0] == "add":
            val = regs[parts[2]] if parts[2] in regs.keys() else int(parts[2])
            regs[parts[1]] = regs[parts[1]] + val

            if parts[1] == 'z' and parts[2] == 'y':
                zs.append(regs['z'])
        elif parts[0] == "mul":
            val = regs[parts[2]] if parts[2] in regs.keys() else int(parts[2])
            regs[parts[1]] = regs[parts[1]] * val
        elif parts[0] == "div":
            val = regs[parts[2]] if parts[2] in regs.keys() else int(parts[2])
            regs[parts[1]] = regs[parts[1]] // val
        elif parts[0] == "mod":
            val = regs[parts[2]] if parts[2] in regs.keys() else int(parts[2])
            regs[parts[1]] = regs[parts[1]] % val
        elif parts[0] == "eql":
            val = regs[parts[2]] if parts[2] in regs.keys() else int(parts[2])
            regs[parts[1]] = 1 if regs[parts[1]] == val else 0

    return regs['z'] == 0, zs

pos = 0
LEN = 18
C = []

for k in range(14):
    c1 = int(data[pos + 4].split(" ")[2])
    c2 = int(data[pos + 5].split(" ")[2])
    c3 = int(data[pos + 15].split(" ")[2])
    C.append((c1, c2, c3))
    pos += LEN

diffs = {}

def run_rev(num):
    oz = 0
    z = x = y = 0
    for i,w in enumerate(num):
        w = int(w)
        c1,c2,c3 = C[i]
        # z % 26 = z - z // 26
        # z - z // 26 + c2 == w
        # z // 26 = z + c2 - w
        if z % 26 + c2 == w: # always false since z always %26==0 and no c2 in 1..9
            # prev z is 26*z + w + c3
            # so w_old + old_c3 + c2 = w
            # diffs[i] = c3 + c2
            
            z = z // c1
        else:
            if (c1 == 26):
                z = z - z%26 + w + c3 # next %26 will give w + c3
            else:
                z = 26*z + w + c3  # next %26 will also give w + c3
    return z

c3s = []
shifts = {}
for i,c in enumerate(C):
    c1,c2,c3 = c
    if c1 == 26:
        ii, old_c3 = c3s.pop()
        shifts[i] = (old_c3 + c2, ii)
    else:
        c3s.append((i, c3))


#{4: (-5, 3), 7: (-4, 6), 9: (2, 8), 
# 10: (8, 5), 11: (5, 2), 12: (-2, 1), 13: (6, 0)}

minn = None
maxx = 0
for i0 in [1,2,3,4,5,6,7,8,9]:
    for i1 in [1,2,3,4,5,6,7,8,9]:
        for i2 in [1,2,3,4,5,6,7,8,9]:
            for i3 in [1,2,3,4,5,6,7,8,9]:
                for i5 in [1,2,3,4,5,6,7,8,9]:
                    for i6 in [1,2,3,4,5,6,7,8,9]:
                        for i8 in [1,2,3,4,5,6,7,8,9]:
                            i4 = max(1, i3 - 5)
                            i7 = max(1, i6 - 4)
                            i9 = min(9, i8 + 2)
                            i10 = min(9, i5 + 8)
                            i11 = min(9, i2 + 5)
                            i12 = max(1, i1 - 2)
                            i13 = min(9, i0 + 6)

                            num = str(i0)+str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)+str(i8)+str(i9)+str(i10)+str(i11)+str(i12)+str(i13)
                            if run_rev(num) == 0:
                                if minn is None:
                                    minn = num
                                maxx = num
        print(num)

print(run(maxx), run(minn))
print(maxx)
print(minn)
