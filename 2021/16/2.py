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

def parse_packets(st, count = 10000000000000000):
    values = []
    global versum
#    print("Packet: ", st)
    pos = 0
#    print("Total bits: ", len(st))
    cnt = 0
    while pos + 7 < len(st) and cnt < count:
        cnt += 1
        ver = int(st[pos:pos+3], 2)
        versum += ver
        pos += 3
        typ = int(st[pos:pos+3], 2)
        pos += 3
#        print("Version", ver, "Type", typ)
        length = 6
        if typ == 4:
#            print("Literal")
            res = 0
            while True:
                pref = st[pos]
                pos += 1
                length += 1
                val = st[pos:pos+4]
#                print("p", pref, val)
                pos += 4
                length += 4
                res *= 16
                res += int(val, 2)
                if pref == "0":
#                    print("literal", res)
                    print(f"{res} ", end = '')
                    values.append(res)
                    break
        else:
#            print("Operator ", typ)
            lenid = int(st[pos], 2)
            pos += 1
#            print("length id", lenid)
            if lenid == 0:
                sublen = int(st[pos:pos+15], 2)
                pos += 15
                subpac = st[pos:pos+sublen]
                (p, myvals) = parse_packets(subpac, 1000000000)
                pos += sublen
            else:
                pacnum = int(st[pos:pos+11], 2)
                pos += 11
#                print(pacnum, "packets of N bits")
                myvals = []
                for k in range(pacnum):
                    subp = st[pos:]
                    (pos_diff, v) = parse_packets(subp, 1)
#                    print("Parsed", cnt, "bytes")
                    pos += pos_diff
                    myvals += v

            if typ == 0:
                print("+ ", end = '')
                values.append(sum(myvals))
            elif typ == 1:
                print("* ", end = '')
                res = 1
                for v in myvals:
                    res *= v
                values.append(res)
            elif typ == 2:
                print("min ", end = '')
                values.append(min(myvals))
            elif typ == 3:
                print("max ", end = '')
                values.append(max(myvals))
            elif typ == 5:
                print("> ", end = '')
                values.append(1 if myvals[0] > myvals[1] else 0)
            elif typ == 6:
                print("< ", end = '')
                values.append(1 if myvals[0] < myvals[1] else 0)               
            elif typ == 7:
                print("== ", end = '')
                values.append(1 if myvals[0] == myvals[1] else 0)  
#    print(pos, values, st)
    return pos, values

_, vvv = parse_packets(st)
result = vvv[0]
print()
print(vvv)
print(result)
pyperclip.copy(result)