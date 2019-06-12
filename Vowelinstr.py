u=input()
v=len(u)
w=0
for i in range(v):
	if(u[i] in('a','e','i','o','u')):
		w+=1
if(w>0):
	print("yes")
else:
	print("no")
