fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

energy = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

#initial = list(list([ ' ' ] * 11) + [ 'A', 'D', 'C', 'D', 'B', 'A', 'B', 'C' ])
initial = list([ ' ' ] * 11) + [ 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'A' ]

room1 = [ 11, 12 ]
room2 = [ 13, 14 ]
room3 = [ 15, 16 ]
room4 = [ 17, 18 ]

history = []
result = 0

results = []

def get_possible(energ, mapp):
    possible = []
    for i,c in enumerate(mapp):
        if c != ' ':
            if i < 11:
                # try left
                for j in range(i-1, -1, -1):
                    if j < 0:
                        break
                    if mapp[j] != ' ':
                        break
                    if j in [ 2, 4, 6, 8] and mapp[j + 9] == ' ' and (mapp[j+10] == c or mapp[j+10] == ' '): # go to the top of the room from right
                        newl = list(mapp)
                        newl[i] = ' '
                        newl[j + 9] = c
                        possible.append((newl, energ + (i - j + 1) * energy[c]))
                    if j in [ 2, 4, 6, 8] and mapp[j + 9] == ' ' and mapp[j+10] == ' ': # go to the bottom of the room from right
                        newl = list(mapp)
                        newl[i] = ' '
                        newl[j + 10] = c
                        possible.append((newl, energ + (i - j + 2) * energy[c]))

                # try right
                for j in range(i+1, 11):
                    if j > 10:
                        break
                    if mapp[j] != ' ':
                        break
                    if j in [ 2, 4, 6, 8] and mapp[j + 9] == ' ' and (mapp[j+10] == c or mapp[j+10] == ' '): # go to the top of the room from right
                        newl = list(mapp)
                        newl[i] = ' '
                        newl[j + 9] = c
                        possible.append((newl, energ + (j - i + 1) * energy[c]))
                    if j in [ 2, 4, 6, 8] and mapp[j + 9] == ' ' and mapp[j+10] == ' ': # go to the bottom of the room from right
                        newl = list(mapp)
                        newl[i] = ' '
                        newl[j + 10] = c
                        possible.append((newl, energ + (j - i + 2) * energy[c]))
            else: # room
                if i in [ 11, 13, 15, 17 ]: # top and can exit
                    for j in range(i - 9, 11): # try exit and go right
                        if mapp[j] != ' ':
                            break
                        if mapp[j] in [ 2, 4, 6, 8]:
                            continue

                        newl = list(mapp)
                        newl[i] = ' '
                        newl[j] = c
                        possible.append((newl, energ + (j - (i - 9) + 1) * energy[c]))

                    for j in range(0, i - 9): # try exit and go left
                        if mapp[j] != ' ':
                            break
                        if mapp[j] in [ 2, 4, 6, 8]:
                            continue

                        newl = list(mapp)
                        newl[i] = ' '
                        newl[j] = c
                        possible.append((newl, energ + ((i - 9) - j + 1) * energy[c]))
                if i in [ 12, 14, 16, 18 ] and mapp[i-1] == ' ': # bottom and can exit
                    for j in range(i - 9, 11): # try exit and go right
                        if mapp[j] != ' ':
                            break
                        if mapp[j] in [ 2, 4, 6, 8]:
                            continue

                        newl = list(mapp)
                        newl[i] = ' '
                        newl[j] = c
                        possible.append((newl, energ + (j - (i - 9) + 2) * energy[c]))

                    for j in range(0, i - 9): # try exit and go left
                        if mapp[j] != ' ':
                            break
                        if mapp[j] in [ 2, 4, 6, 8]:
                            continue

                        newl = list(mapp)
                        newl[i] = ' '
                        newl[j] = c
                        possible.append((newl, energ + ((i - 9) - j + 2) * energy[c]))
    return possible

a = energy['A']
b = energy['B']
c = energy['C']
d = energy['D']

print(2*a+4*b+3*a+5*c+3*a+2*b+5*c+8*d+3*b+9*d+3*a+6*b+9*a)
print(9*a+4*b+3*b+9*a+9*a+7*c+7*c+4*b+5*d+5*b+6*b+7*b+6*b+3*a+7*c+7*c+9*d+33*d+10*a+9*a+9*a)

exit()

# Some infinite bullshit below that works sooo long that I managed to solve both parts manually until even some non-optimal solution was found
# God bless cell drag'n'drop in Excel tables!

positions = [ (initial, 0) ]
seen = set([])
while positions:
    p, energ = positions.pop(0)
    pp = tuple(p)
    if pp in seen:
        continue
    seen.add(pp)

    if p[11] == 'A' and p[12] == 'A' and p[13] == 'B' and p[14] == 'B' and p[15] == 'C' and p[16] == 'C' and p[17] == 'D' and p[18] == 'D':
        results.append((p,energ))
        print(len(positions), len(seen), energ, p)
    else:
        possib = get_possible(energ, p)
        positions += possib

print(results)
print(seen)
result = min([ e for _, e in results ])
pyperclip.copy(result)

#print()