f = open("01.txt", "r")
lines = map(lambda x: int(x), f.readlines())

for l in lines:
	for m in lines:
		for n in lines:
			if l+m+n == 2020:
				print l,m,n, l*m*n
