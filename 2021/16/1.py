fname = "data.txt"
#fname = "test.txt"

import os, sys
import pyperclip
from collections import Counter

result = 0
versum = 0


with open(fname) as f:
    data = list(map(lambda x: x.strip(), f.readlines()))

st = ""

for p in data[0]:
    n = format(int(p, 16), '04b')
    st += n

rrr = 0

def parse_packets(st, count = -1):
    global versum
    print("Packet: ", st)
    pos = 0
    print("Total bits: ", len(st))
    while pos + 7 < len(st):
        ver = int(st[pos:pos+3], 2)
        versum += ver
        pos += 3
        typ = int(st[pos:pos+3], 2)
        pos += 3
        print("Version", ver, "Type", typ)
        length = 6
        if typ == 4:
            print("Literal")
            res = 0
            while True:
                pref = st[pos]
                pos += 1
                length += 1
                val = st[pos:pos+4]
                print("p", pref, val)
                pos += 4
                length += 4
                res *= 16
                res += int(val, 2)
                if pref == "0":
                    print("literal", res)
                    break
        else:
            print("Operator")
            lenid = int(st[pos], 2)
            pos += 1
            print("length id", lenid)
            if lenid == 0:
                sublen = int(st[pos:pos+15], 2)
                pos += 15
                subpac = st[pos:pos+sublen]
                parse_packets(subpac, 1)
                pos += sublen
            else:
                pacnum = int(st[pos:pos+11], 2)
                pos += 11
                print(pacnum, "packets of N bits")
                for k in range(pacnum):
                    subp = st[pos:]
                    cnt = parse_packets(subp, 1)
                    print("Parsed", cnt, "bytes")
                    pos += cnt
    return pos

parse_packets(st, True)
result = versum
print(result)
pyperclip.copy(result)