fname = "data.txt"
#fname = "test.txt"

# only signal wires b and g are turned on

import os, sys, itertools
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x, f.readlines()))

count1 = 0
count4 = 0
count7 = 0
count8 = 0

for d in data:
    segs, res = d.split("|")
    inp = res.split()
    for l in inp:
        if len(l) == 2:
            count1 += 1
        if len(l) == 4:
            count4 += 1
        if len(l) == 3:
            count7 += 1
        if len(l) == 7:
            count4 += 1

result = count1 + count4 + count7 + count8

print(result)
pyperclip.copy(result)