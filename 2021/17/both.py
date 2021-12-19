fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

# TODO target area: 
xmin=124
xmax=174
ymin=-123
ymax=-86

#xmin=20
#xmax=30
#ymin=-10
#ymax=-5

velx = 7
vely = 2

mayyy = -10000000000000000000

cnt = 0

for vx in range(0, 200):
    for vy in range(-200, 200):
        x = 0
        y = 0
        velx = vx
        vely = vy
        highest = -100000000000
        for step in range(1000):
  #          print(step, x, y)
            x += velx
            y += vely
            if velx > 0:
                velx -= 1
            elif velx < 0:
                velx += 1
            vely -= 1

#            print(y,highest)

            if y > highest:
                highest = y

            if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
#                print(step, "Within", highest)
                if mayyy < highest:
                    mayyy = highest
                cnt += 1
                break

result = mayyy
print(result)
print(cnt)
pyperclip.copy(result)