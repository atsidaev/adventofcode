fname = "data.txt"
#fname = "test.txt"

import os, sys, math

result = 0

with open(fname) as f:
    data = list(map(lambda x: x, f.readlines()))


fishes = data[0].split(',')
fishes = [ int(x) for x in fishes ]

result = 0

counts = [ 0 ] * 9
for f in fishes:
    counts[f] += 1

print(counts)

for n in range(256):
    today = counts[0]
    counts = counts[1:] + [ today ]
    counts[6] += today

print(counts, sum(counts))

print(result)