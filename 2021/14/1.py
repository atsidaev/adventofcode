fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))


template = data[0]

preobr = [ m.split(" -> ") for m in data[2:] ]



for steps in range(40):
    new_temp = ""
    for i in range(len(template) - 1):
        pair = template[i:i+2]
#        print(pair)
        for l,r in preobr:
            if pair == l:
                new_temp += pair[0] + r
    new_temp += template[-1]
    print(new_temp)
    template = new_temp

a = dict([])
for l in template:
    if not l in a:
        a[l] = 0
    a[l] += 1

min = min(a.values())
max = max(a.values())

result = max - min
print(result)
pyperclip.copy(result)