fname = "data.txt"
# fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

scanner = []
scanners = []
num = 0
for d in data:
    if "scanner" in d:
        if len(scanner) > 0:
            scanners.append(scanner)
            scanner = []
            num += 1
    elif d != '':
        scanner.append([ int(x) for x in d.split(",") ])

scanners.append(scanner)
print(scanners)

def align_coord(coords1, coords2):
    possible_shifts = []
    for c1 in coords1:
        for c2 in coords2:
            shift = c2 - c1
            shifted2 = [ c - shift for c in coords2 ]
            cnt = 0
            for sc in shifted2:
                if sc in coords1:
                    cnt+=1

            if cnt >= 12:
                possible_shifts.append((shift, shifted2))
    return possible_shifts

def align(s1, s2):
    possibilities = [ [], [], [] ]
    for axis1 in range(3):
        for axis2 in range(3):
            for sign in [1,-1]:
                possible_shifts = align_coord([ x[axis1] for x in s1 ], [ sign * x[axis2] for x in s2 ])
                if len(possible_shifts) > 0:
                    possibilities[axis1] += possible_shifts
    
    if [] in possibilities:
        return []

    for sh1, p1 in possibilities[0]:
        for sh2, p2 in possibilities[1]:
            for sh3, p3 in possibilities[2]:
                cnt = 0
                points = []
                for n in range(len(p1)):
                    point = [ p1[n], p2[n], p3[n] ]
                    points.append(point)
                    if point in s1:
                        cnt += 1

                if cnt >= 12:
                    return (sh1, sh2, sh3), points
    return []

map = Counter()

for p in scanners[0]:
    map[(p[0], p[1], p[2])] += 1

# aligned with 0
aligned_scanners = [ scanners[0] ]
aligned_indeces = [ 0 ]
coords = [ (0,0,0) ]
while len(aligned_scanners) < len(scanners):
    for als in aligned_scanners:
        for s in range(len(scanners)):
            if s in aligned_indeces:
                continue

            print("Testing scanner ", s)

            aaa = align(als,scanners[s])
            if len(aaa) == 0:
                continue

            shift, aligned = aaa

            aligned_indeces.append(s)
            aligned_scanners.append(aligned)
            coords.append(shift)

            for p in aligned:
                if p[0] == -739:
                    print("Wrong")
                    print(s)
                    print(aligned)
                    print("End wrong")
                map[(p[0], p[1], p[2])] += 1

result = len(map)
print(coords)

maxx = 0
for c1x, c1y, c1z in coords:
    for c2x, c2y, c2z in coords:
        dx = c2x - c1x
        dy = c2y - c1y
        dz = c2z - c1z
        dst = abs(dx) + abs(dy) + abs(dz)
        if dst > maxx:
            maxx = dst

print(result)
result = maxx
print(result)
pyperclip.copy(result)