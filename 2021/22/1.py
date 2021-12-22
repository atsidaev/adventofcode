fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

engine = set([])

for l in data:
    act, c = l.split(' ')
    xx, yy, zz = c.split(',')
    xxx = xx.split('=')[1]
    yyy = yy.split('=')[1]
    zzz = zz.split('=')[1]
    xs = [ int(x) for x in xxx.split("..") ]
    ys = [ int(x) for x in yyy.split("..") ]
    zs = [ int(x) for x in zzz.split("..") ]
    print(xs, ys, zs)

    if xs[0] < -50 or xs[1] >= 50 or ys[0] < -50 or ys[1] >= 50 or zs[0] < -50 or zs[1] >= 50:
        continue

    for x in range(xs[0], xs[1] + 1):
        for y in range(ys[0], ys[1] + 1):
            for z in range(zs[0], zs[1] + 1):
                if act == "on":
                    engine.add((x,y,z))
                elif act == "off":
                    if (x,y,z) in engine:
                        engine.remove((x,y,z))
                else:
                    raise 123

result = len(engine)

print(result)
pyperclip.copy(result)