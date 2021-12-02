fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip

result = 0

with open(fname) as f:
    data = map(lambda x: x, f.readlines())

# TODO

print(result)
pyperclip.copy(result)