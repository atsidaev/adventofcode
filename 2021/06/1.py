fname = "data.txt"
#fname = "test.txt"

import os, sys
#import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x, f.readlines()))


fishes = data[0].split(',')
fishes = [ int(x) for x in fishes ]

result = len(fishes)

for n in range(80):
    #print(fishes)
    fishes = [ x - 1 for x in fishes]
    new = len(list(filter(lambda x: x == -1, fishes)))
    result += new
    fishes += [ 8 ] * new
    fishes = [ 6 if x == -1 else x for x in fishes ]

print(result)
#pyperclip.copy(result)