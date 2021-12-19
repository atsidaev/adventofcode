f = open("01.txt", "r")
lines = list(map(lambda x: int(x), f.readlines()))

for l in lines:
	for m in lines:
		for n in lines:
			if l+m+n == 2020:
				print(l,m,n)
				print(l*m*n)
