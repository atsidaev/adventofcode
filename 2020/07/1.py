import re

with open("test2.txt", "r") as f:
	lines = f.readlines()
	
lines = map(lambda x: x.split("contain"), lines)


lines = [ [l[0].strip(), l[1].split(",")] for l in lines ]

for i in range(len(lines)):
	lines[i][0] = lines[i][0].replace(" bag", "")[:-1]
	for k in range(len(lines[i][1])):
		lines[i][1][k] = lines[i][1][k].strip()
		if lines[i][1][k] == "no other bags.":
			continue
		m = re.match("\d+ (.*) bags?", lines[i][1][k])
		if not m:
			raise Exception(lines[i][1][k])
		lines[i][1][k] = m.groups(1)[0]

result = {}

def process(bag, lines):
	wh = list(filter(lambda x: bag in x[1], lines))
	print(wh)
	for w in wh:
		print(w)
		if not str(w) in result.keys():
			result[w[0]] = 1
			process(w[0], lines)

process("shiny gold", lines)
print(len(result))

