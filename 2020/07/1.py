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
		m = re.match("(\d+) (.*) bags?", lines[i][1][k])
		if not m:
			raise Exception(lines[i][1][k])
		lines[i][1][k] = (int(m.groups(1)[0]), m.groups(1)[1])

result = {}

def process(bag, lines):
	result = 1
	wh = list(filter(lambda x: x[0] == bag, lines))
	print(wh[0])
	if "no other bags." in wh[0][1]:
		return result
	for (n,w) in wh[0][1]:
		result += n * process(w, lines)
	return result
	
print(process("shiny gold", lines) - 1)
