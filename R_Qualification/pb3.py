f = open('input3.in', 'r')
g = open('output3.in', 'w')
line = f.readline()
T = int(line)
check = "HACKERCUP"
for i in range(T):
	line = f.readline()
	s = str(line)
	counter = [0,0,0,0,0,0,0,0,0]
	for char in s:
		if char in check:
			counter[check.index(char)] += 1 
	counter[6] = counter[2] / 2
	counter[2] = counter[2] - counter[6]
	counter.sort()
	g.write('Case #' + str(i+1) + ': ' + str(counter[0]) + '\n')
f.close()
g.close()	
