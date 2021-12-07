fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x, f.readlines()))

min = 100000000000
min_pos = -1
data = [ int(x) for x in data[0].split(',') ]
for pos in range(max(data)):
    diffs = [ abs(x - pos) for x in data ]
    s = sum(diffs)
    if s < min:
        min = s
        min_pos = pos

diffs = [ abs(x - min_pos) for x in data ]

print(min_pos, min)
pyperclip.copy(result)