fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = map(lambda x: x.strip(), f.readlines())

x = 0
z = 0

for d in data:
    parts = d.split(' ')
    val = int(parts[1])
    if (parts[0] == "forward"):
        x += val
    elif (parts[0] == "up"):
        z -= val
    elif (parts[0] == "down"):
        z += val
    else:
        raise Exception(parts)

print(x,z)
result = x*z
print(result)
pyperclip.copy(result)