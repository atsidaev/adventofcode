fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))


template = data[0]

preobr = [ m.split(" -> ") for m in data[2:] ]

counts = dict([])
for t in template:
    if not t in counts:
        counts[t] = 0
    counts[t] += 1

for a,t in preobr:
    if not t in counts:
        counts[t] = 0

pairsd = dict([])
for a,t in preobr:
    pairsd[a] = 0

for i in range(len(template) - 1):
    pair = template[i:i+2]
    pairsd[pair] += 1

for steps in range(40):
    new_pairs = dict([])
    lett = dict([])
    for pair in pairsd:
        for l,r in preobr:
            if pair == l:
                new1 = l[0] + r
                new2 = r + l[1]

 #               print(new1, new2)

                if not new1 in new_pairs:
                    new_pairs[new1] = 0

                if not new2 in new_pairs:
                    new_pairs[new2] = 0

                new_pairs[new1] += pairsd[pair]
                new_pairs[new2] += pairsd[pair]

                if not l[0] in lett:
                    lett[l[0]] = 0
                lett[l[0]] += pairsd[pair]

                if not r in lett:
                    lett[r] = 0
                lett[r] += pairsd[pair]

    if not template[-1] in lett:
        lett[template[-1]] = 0
    lett[template[-1]] += 1

#    print(new_pairs)

    mmin = min(lett.values())
    mmax = max(lett.values())
    result = mmax - mmin

    pairsd = new_pairs

print(result)
pyperclip.copy(result)