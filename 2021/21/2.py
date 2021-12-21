fname = "data.txt"
fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0

ppp1 = 8
ppp2 = 1

WINS = dict()

def roll(pp1, pp2, sscore1, sscore2):
    if (pp1, pp2, sscore1, sscore2) in WINS:
        return WINS[(pp1, pp2, sscore1, sscore2)]

    if sscore1 >= 21:
        return (1,0)
    elif sscore2 >= 21:
        return (0,1)
    else:
        total = (0,0)
        for dice1 in [ 1, 2, 3 ]:
            for dice2 in [ 1, 2, 3 ]:
                for dice3 in [ 1, 2, 3 ]:
                    p1 = pp1
                    score1 = sscore1
                    summ1 = dice1 + dice2 + dice3
                    p1 += summ1
                    while p1 > 10:
                        p1 -= 10
                    score1 += p1

                    for dice4 in [ 1, 2, 3 ]:
                        for dice5 in [ 1, 2, 3 ]:
                            for dice6 in [ 1, 2, 3 ]:
                                p2 = pp2
                                score2 = sscore2
                                summ2 = dice4 + dice5 + dice6
                                p2 += summ2
                                while p2 > 10:
                                    p2 -= 10
                                score2 += p2

                                w1,w2 = roll(p1, p2, score1, score2)
                                total = (total[0] + w1, total[1] + w2)

        WINS[(pp1, pp2, sscore1, sscore2)] = total
        return total

def roll2(pp1, pp2, sscore1, sscore2):
    if (pp1, pp2, sscore1, sscore2) in WINS:
        return WINS[(pp1, pp2, sscore1, sscore2)]

    if sscore1 >= 21:
        return (1,0)
    elif sscore2 >= 21:
        return (0,1)
    else:
        total = (0,0)
        for dice1 in [ 1, 2, 3 ]:
            for dice2 in [ 1, 2, 3 ]:
                for dice3 in [ 1, 2, 3 ]:
                    p1 = pp1
                    score1 = sscore1
                    summ1 = dice1 + dice2 + dice3
                    p1 += summ1
                    while p1 > 10:
                        p1 -= 10
                    score1 += p1

                    w1,w2 = roll2(pp2, p1, sscore2, score1)
                    total = (total[0] + w2, total[1] + w1)

        WINS[(pp1, pp2, sscore1, sscore2)] = total
        return total

result = max(roll2(ppp1, ppp2, 0, 0))

print((444356092776315, 341960390180808) in WINS.values())
print(result)
pyperclip.copy(result)