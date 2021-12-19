fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

numbers = list(filter(lambda x: int(x), data[0].split(",")))

cards = []
card = []
for line in data[2:]:
    if line != '':
        card.append([int(x) for x in line.split()])
    else:
        cards.append(card)
        card = []

cards.append(card)

print(cards)

for num_cnt in range(len(numbers)):
    cur_numbers = [int(x) for x in numbers[0:num_cnt]]
    
    for c in cards:
        for l in c:
            #print(cur_numbers, len(list(filter(lambda x: x in cur_numbers, l))), l)
            if len(list(filter(lambda x: x in cur_numbers, l))) == len(l):
                sum1 = 0
                for k in c:
                    for n in k:
                        if not n in cur_numbers:
                            print(n)
                            sum1 += n
                print(c, cur_numbers, sum1)
                print(cur_numbers[-1] * sum1)
                exit(0)

print(result)
pyperclip.copy(result)