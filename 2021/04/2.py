fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

numbers = list(map(lambda x: int(x), data[0].split(",")))

cards = []
card = []
for line in data[2:]:
    if line != '':
        card.append([int(x) for x in line.split()])
    else:
        cards.append(card)
        card = []

cards.append(card)

def win_lines_cnt(numbers, card):
    won = False
    remaining = []
    for l in card:
        #print(cur_numbers, len(list(filter(lambda x: x in cur_numbers, l))), l)
        win_numbers1 = set(filter(lambda x: x in numbers, l))
        if len(win_numbers1) == len(l):
            won = True

    for col in range(len(card[0])):
        col_nums = [ x[col] for x in card ]
        win_numbers2 = set(filter(lambda x: x in numbers, col_nums))
        if len(win_numbers2) == len(col_nums):
            won = True

    sum1 = 0
    for k in card:
        for n in k:
            if not n in numbers:
                sum1 += n
    
    return won, sum1

for num_cnt in range(len(numbers)):
    cur_numbers = [int(x) for x in numbers[0:num_cnt+1]]
    print("vypalo", cur_numbers[-1])

    non_win = list(filter(lambda x: win_lines_cnt(cur_numbers, x)[0] == 0, cards))
    if len(non_win) == 1:
        print("one left")
        cards = non_win
        last = cards[0]
    
    if len(non_win) == 0:
        print("winner", last)
        print(win_lines_cnt(cur_numbers, last)[1] * cur_numbers[-1])
        exit()

print(result)
pyperclip.copy(result)