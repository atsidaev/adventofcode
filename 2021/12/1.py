fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

caves = dict([])

for l in data:
    beg, end = l.split("-")
    if not beg in caves:
        caves[beg] = []
    if not end in caves:
        caves[end] = []
    caves[beg].append(end)
    caves[end].append(beg)

def visit(path):
    last = path[-1]
    result = []

    for possible_way in caves[last]:
        if possible_way in path and possible_way.lower() == possible_way:
            continue
        result.append( path + [ possible_way ] )

    return result

paths = [[ 'start' ]]
count = 0
while paths:
    cur_path = paths.pop(0)
    ways = visit(cur_path)
    for w in ways:
        if w[-1] == 'end':
  #          print(w)
            count += 1
        else:
            paths.append(w)
        
result = count
pyperclip.copy(result)
print(result)