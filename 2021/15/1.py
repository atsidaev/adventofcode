fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

cnt = (len(data)) * (len(data[0]))
matrix = [ [0] * cnt ] * cnt

M = 100000000
mmap = [ [ int(l) for l in d ] for d in data ]
dst = [ [ M for i in l ] for l in mmap ]

# dist, (x, y)
p = (0, (0, 0))
verts = [p]
while verts:
    d, (x,y) = verts.pop(0)
    for nx,ny in [ (x-1, y), (x+1, y), (x, y-1), (x, y+1) ]:
        if nx >= 0 and nx < len(mmap[0]) and ny >= 0 and ny < len(mmap):
            nd = d + mmap[ny][nx]
#            print(nx, ny, nd, dst[ny][nx])
            if nd < dst[ny][nx]:
                dst[ny][nx] = nd
                verts.append((nd, (nx,ny)))
    verts.sort()
#    print(verts)
#    print(dst)

result = dst[len(mmap) - 1][len(mmap[0]) - 1]
print(result)
pyperclip.copy(result)