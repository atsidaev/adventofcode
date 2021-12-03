fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

cnt = [-1] * 100

for l in data:
    for k in range(len(l)):
        if l[k] == "1":
            cnt[k]+=1

a = cnt[0:len(l)]

length = len(data)
bits = len(data[0])
print(length, a)

v = "".join([ "1" if c >= length/2 else "0" for c in a ])
e = "".join([ "0" if c >= length/2 else "1" for c in a ])
print("result", v, e, int(v,2) * int(e,2))