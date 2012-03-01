f = open('input1.in', 'r')
g = open('output1.txt', 'w')
line = f.readline()
T = int(line)
for test in range(T):
	line = f.readline()
	s = str(line)
	s = s.rstrip()
	st = s.split(' ')
	W = int(st[0])
	H = int(st[1])
	st.remove(str(W))
	st.remove(str(H))
	l = []
	k = []
	for word_i in range(len(st)):
		l_aux = len(st[word_i])
		l.append(l_aux)
		ka = []
		ka_left = range(1,word_i+1)
		ka_right = range(1,len(st)-word_i)
		if ka_left and ka_right:
			for i in range(len(ka_left)):
				for j in range(len(ka_right)):
					ka.append(ka_left[i] + ka_right[j])
		elif ka_left:
			ka = ka_left
		elif ka_right:
			ka = ka_right
		ka = map(lambda x: x + 1, ka)
		if not ka:
			ka.append(1)
		k.append(ka)
		for cursor in range(word_i+1,len(st)):
			l_aux = l_aux + len(st[cursor]) + 1
			l.append(l_aux)
			ka = []
			ka_left = range(1,word_i+1)
			ka_right = range(1,len(st)-cursor)
			if ka_left and ka_right:
				for i in range(len(ka_left)):
					for j in range(len(ka_right)):
						ka.append(ka_left[i] + ka_right[j])
			elif ka_left:
				ka = ka_left
			elif ka_right:
				ka = ka_right
			ka = map(lambda x: x + 1, ka)
			if not ka:
				ka.append(1)
			k.append(ka)
	print st
	print l
	print k
	m_font = 0
	for l_i in range(len(l)):
		for k_i in range(len(k[l_i])):
			m_font = max(m_font, min(W/l[l_i],H/k[l_i][k_i]))
			if test+1 == 3:
				print m_font, '\n'
	g.write('Case #' + str(test+1) + ': ' + str(m_font) + '\n')
f.close()
g.close()
	
