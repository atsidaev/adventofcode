fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

engine = []
esects = []
error = 0

def volume(xs,ys,zs):
    return (xs[1] - xs[0] + 1) * (ys[1] - ys[0] + 1) * (zs[1] - zs[0] + 1)

cnt = 10

def intersect(x1, y1, z1, x2, y2, z2):
    global cnt
    # 1 - input data
    # 2 - stored cube from array

    if x1[0] > x2[1] or x1[1] < x2[0] or y1[0] > y2[1] or y1[1] < y2[0] or z1[0] > z2[1] or z1[1] < z2[0]:
        return [ (x2,y2,z2) ]

    # bounding cubes of intersection
    # remove left & right
    xxx1 = [x2[0], x1[0] - 1]
    xxx2 = [x1[1] + 1, x2[1]]

    # remove near & far
    #x_nox = x1[0], x2[0]
    x_nox = [ max(x1[0], x2[0]), min(x1[1], x2[1]) ]
    #print(xxx1, xxx2, x_nox)

    y_noxy = [ max(y2[0], y1[0]), min(y2[1], y1[1]) ]

    remains = []
    if x1[0] > x2[0]: # left
        remains.append((xxx1, y2, z2))
    if x1[1] < x2[1]: # right
        remains.append((xxx2, y2, z2))
    if y1[0] > y2[0]: # near wihtout x
        remains.append((x_nox, (y2[0], y1[0] - 1), z2))
    if y1[1] < y2[1]: # far wihtout x
        remains.append((x_nox, [y1[1] + 1, y2[1]], z2 ))
    if z1[0] > z2[0]: # top without xy
        remains.append((x_nox, y_noxy, [ z2[0], z1[0] - 1 ]))
    if z1[1] < z2[1]: # bot without xy
        remains.append((x_nox, y_noxy, [ z1[1] + 1, z2[1] ]))

    return remains

for iii,l in enumerate(data):
    act, c = l.split(' ')
    xx, yy, zz = c.split(',')
    xxx = xx.split('=')[1]
    yyy = yy.split('=')[1]
    zzz = zz.split('=')[1]
    xs = [ int(x) for x in xxx.split("..") ]
    ys = [ int(x) for x in yyy.split("..") ]
    zs = [ int(x) for x in zzz.split("..") ]

    # if xs[0] < -50 or xs[1] >= 50 or ys[0] < -50 or ys[1] >= 50 or zs[0] < -50 or zs[1] >= 50:
    #     continue
    
    #if act == "off":
    new_engine = []
    for i, e in enumerate(engine):
        exs, eys, ezs = e
        
        r = intersect(xs, ys, zs, exs, eys, ezs)
        if cnt > 0:
            print(xs, ys, zs)
            print("    E:", exs, eys, ezs)
            cnt -= 1
        new_engine += r
    engine = new_engine

    if act == "on":
        engine.append((xs,ys,zs))

    #print(iii, len(engine))

result = sum([ volume(ex, ey, ez) for ex, ey, ez in engine ])

# print(engine)

print(result)
pyperclip.copy(result)