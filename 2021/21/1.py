fname = "data.txt"
fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

dice = 0
cnt = 0

p1 = 8
p2 = 1

score1 = 0
score2 = 0

while True:
    summ = 0

    for k in range(3):
        dice += 1
        cnt += 1
        if dice == 101:
            dice = 1

  #      print(dice)

        summ += dice
        
    p1 += summ
    while p1 > 10:
        p1 -= 10
    score1 += p1
    
    if score1 >= 1000:
        result = cnt * score2
        break

    summ = 0

    for k in range(3):
        dice += 1
        cnt += 1
        if dice == 101:
            dice = 1

   #     print(dice)

        summ += dice
        
    p2 += summ
    while p2 > 10:
        p2 -= 10
    score2 += p2
    
    if score2 >= 1000:
        result = cnt * score1
        break

print(cnt, score1, score2)

print(result)
pyperclip.copy(result)