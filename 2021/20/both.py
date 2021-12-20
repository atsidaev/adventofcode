fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

enc = data[0]

mapp = data[2:]
pic = dict()
for y in range(len(mapp)):
    for x in range(len(mapp[0])):
        pic[(x,y)] = mapp[y][x] == '#'

def calc(pic, n):
    for k in range(n):
        minx = min([ x for x,y in pic.keys() ])
        maxx = max([ x for x,y in pic.keys() ])
        miny = min([ y for x,y in pic.keys() ])
        maxy = max([ y for x,y in pic.keys() ])

        pic2 = dict()
        out = "0" if enc[0] == '.' or k%2 == 0 else "1"
        for y in range(miny-1, maxy+2):
            for x in range(minx-1, maxx+2):
                #print("#" if (x,y) in pic.keys() and pic[(x,y)] == True else ".", end='')
                alln = [ (x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1) ]
                val = int("".join([ ("1" if pic[p] == True else "0") if p in pic.keys() else out for p in alln ]), 2)
                pic2[(x,y)] = enc[val] == '#'
            #print()
        #print()
        pic = pic2

    return len(list(filter(lambda x: x == True, pic.values())))

print(calc(pic, 2))
print(calc(pic, 50))
pyperclip.copy(result)