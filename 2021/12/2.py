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
 #   print(last)
    result = []

    found_twice = False
    for c in caves.keys():
        if c.lower() == c and c != 'start' and c != 'end':
            if len(list(filter(lambda x: x == c, path))) > 1:
                found_twice = True

    for possible_way in caves[last]:
        if possible_way == 'start':
            continue
        if possible_way != 'end' and possible_way.lower() == possible_way and found_twice and possible_way in path:
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
            count += 1
     #       print(count, w)
        else:
            paths.append(w)
        
result = count
pyperclip.copy(result)
print(result)