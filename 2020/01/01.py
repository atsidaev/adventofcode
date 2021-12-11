f = open("01.txt", "r")
lines = f.readlines()

hash = {}

for l in lines:
	hash[int(l)] = 1

for l in lines:
	n = int(l)
	if (2020-n) in hash:
		print n
		print n * (2020-n)
