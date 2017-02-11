def func(x):
	c=[x[0],1]
	for i in range(1,len(x)):
		if(c[0]==x[i]):	
			c[1]+=1
		elif(c[0]!=x[i]):
			c[1]-=1
			if(c[1]==0):
				c=[x[i],1]
	foo=0
	for i in x:
		if(i==c[0]):
			foo+=1
	if(foo>(len(x)/2)):
		return c[0]	
	else:
		return -1
if(__name__=="__main__"):
	x=map(int,raw_input().split())
	print func(x)
