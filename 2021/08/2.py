fname = "data.txt"
#fname = "test.txt"

# only signal wires b and g are turned on

import os, sys, itertools
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x, f.readlines()))

digits = []
digits.append({ 'a', 'b', 'c', 'e', 'f', 'g' }) # 0
digits.append({ 'c', 'f' }) # 1
digits.append({ 'a', 'c', 'd', 'e', 'g' }) # 2
digits.append({ 'a', 'c', 'd', 'f', 'g' }) # 3
digits.append({ 'b', 'c', 'd', 'f' })           # 4
digits.append({ 'a', 'b', 'd', 'f', 'g' }) # 5
digits.append({ 'a', 'b', 'd', 'e', 'f', 'g' }) # 6
digits.append({ 'a', 'c', 'f' }) # 7
digits.append({ 'a', 'b', 'c', 'd', 'e', 'f', 'g' }) # 8
digits.append({ 'a', 'b', 'c', 'd', 'f', 'g' }) # 9

letters = { 'a', 'b', 'c', 'd', 'e', 'f', 'g' }
num = 0

for l1 in range(7):
    for l2 in range(6):
        for l3 in range(5):
            for l4 in range(4):
                for l5 in range(3):
                    for l6 in range(2):
                        ordered_letters = []
                        iletters = letters

                        letter = list(letters)[l1]
                        ordered_letters.append(letter)
                        letters = letters -  { letter }

                        letter = list(letters)[l2]
                        ordered_letters.append(letter)
                        letters = letters -  { letter }

                        letter = list(letters)[l3]
                        ordered_letters.append(letter)
                        letters = letters -  { letter }

                        letter = list(letters)[l4]
                        ordered_letters.append(letter)
                        letters = letters -  { letter }

                        letter = list(letters)[l5]
                        ordered_letters.append(letter)
                        letters = letters -  { letter }

                        letter = list(letters)[l6]
                        ordered_letters.append(letter)
                        letters = letters -  { letter }

                        letter = list(letters)[0]
                        ordered_letters.append(letter)
                        letters = letters -  { letter }

                        letters = iletters
                        num += 1
                        
                        dic = {}
                        for l in range(len(ordered_letters)):
                            dic[chr(ord('a')+l)] = ordered_letters[l]

                        for d in data:
                            segs, res = d.split("|")
                            left = segs.split()
                            right = res.split()
                            both = left + right

                            need_exit = False

                            for pattern in both:
                                newp = [ dic[k] for k in pattern ]
                                
                                if not set(newp) in digits:
                                    need_exit = True
                                    break

                                if need_exit:
                                    break

                            if not need_exit:
                                #print("All good")

                                numm = ""

                                for r in right:
                                    newr = [ dic[k] for k in r ]

                                    for k in range(len(digits)):
                                        if set(newr) == digits[k]:
                                            numm += str(k)
                           #     print(right, int(numm))
                                result+=(int(numm))

print(result)
pyperclip.copy(result)