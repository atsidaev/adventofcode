fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x, f.readlines()))

def fuel(p1, p2):
    diff = abs(p1 - p2)
    return diff * (1 + diff) / 2

min = 100000000000
min_pos = -1
data = [ int(x) for x in data[0].split(',') ]
for pos in range(max(data)):
    diffs = [ fuel(x, pos) for x in data ]
#    print(diffs)
    s = sum(diffs)
    if s < min:
        min = s
        min_pos = pos

result = min
print(min_pos, result)
pyperclip.copy(result)