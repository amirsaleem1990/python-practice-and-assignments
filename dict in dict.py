a = {'amir' : {'age' : [20,50,30]}}

for b in a:
	q = a[b]
	for m in q:
		print(max(q[m]))
