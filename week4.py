def orangecap(d):
    dict2 = {}
    for k1 in d:
        for k2 in d[k1]:
            dict2[k2] = dict2.get(k2, 0) + d[k1][k2]
    player = max(dict2, key=dict2.get)
    return player, dict2[player]

  
def addpoly(p1,p2):

	m = max(p1[0][1],p2[0][1])

	d1 = {y:x for x,y in p1}
	d2 = {y:x for x,y in p2}
	 
	l = []

	for i in range(m,-1,-1):
		
		if i in d1 and i in d2:
			
			c = d1[i] + d2[i]

			if c:
				l.append((c,i))

		elif i in d1:
		
			l.append((d1[i],i))
		elif i in d2:
		
			l.append((d2[i],i))

	return l 



def multpoly(p1,p2):

	l = []

	for i in p1:
		t = [( x[0]*i[0], x[1]+i[1] ) for x in p2 ]
		l.append(t)


	i = l[0]

	for j in l[1:]:

		i = addpoly(i,j)

	return i 

