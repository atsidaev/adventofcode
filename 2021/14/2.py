fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

template = data[0]

preobr = [ m.split(" -> ") for m in data[2:] ]

counts = Counter()
for t in template:
    counts[t] += 1

for a,t in preobr:
    counts[t] += 0

pairsd = Counter()
for a,t in preobr:
    pairsd[a] = 0

for i in range(len(template) - 1):
    pair = template[i:i+2]
    pairsd[pair] += 1

for steps in range(40):
    new_pairs = Counter()
    lett = Counter()
    for pair in pairsd:
        for l,r in preobr:
            if pair == l:
                new1 = l[0] + r
                new2 = r + l[1]

                new_pairs[new1] += pairsd[pair]
                new_pairs[new2] += pairsd[pair]

                lett[l[0]] += pairsd[pair]
                lett[r] += pairsd[pair]

    lett[template[-1]] += 1

    mmin = min(lett.values())
    mmax = max(lett.values())
    result = mmax - mmin

    pairsd = new_pairs

print(result)
pyperclip.copy(result)