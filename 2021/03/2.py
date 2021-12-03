fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

def get_cnt(arr, most):
    bits = len(arr[0])
    cnt = [0] * bits
    length = len(arr)

    for l in arr:
        for k in range(bits):
            if l[k] == "1":
                cnt[k]+=1

    if most:
        return "".join([ "1" if c >= length/2 else "0" for c in cnt])
    else:
        return "".join([ "0" if c >= length/2 else "1" for c in cnt ])


print(int(get_cnt(data, True), 2) * int(get_cnt(data, False), 2))

bits = len(data[0])
arr1 = data
arr2 = data
for b in range(bits):
    if len(arr1) > 1:
        cnt1 = get_cnt(arr1, True)
        arr1 = list(filter(lambda x: x[b] == cnt1[b], arr1))

    if len(arr2) > 1:
        cnt2 = get_cnt(arr2, False)
        arr2 = list(filter(lambda x: x[b] == cnt2[b], arr2))

    print(b, arr1, arr2)

print(int(arr1[0], 2) * int(arr2[0], 2))
