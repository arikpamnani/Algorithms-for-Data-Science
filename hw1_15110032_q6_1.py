import random
import matplotlib.pyplot as plt
random.seed(10)

# 10 -> seed
# n -> size of hasharray

# function for part(i)
def fullyrandom(k, n, b):
	load = 0
	d = {k:0 for k in range(1, n+1)}
	for x in range(n):
		hx = random.randint(1, n)
		d[hx] += 1
	return max(d.values())

#function for part(ii)
def twochoice(k, n, b):
	d = {k:0 for k in range(1, n+1)}

	for x in range(n):
		fx = random.randint(1, n)
		
		gx = random.randint(1, n)
		
		if d[fx] == d[gx]:
			d[min(fx, gx)] += 1
		elif(d[fx] < d[gx]):
			d[fx] += 1
		else:
			d[gx] += 1
	return max(d.values())

# plot Y v/s X
X = range(10**4, 10**5+1, 10**3)[1:5]
Y1 = []	
Y2 = []
for n in X:	
	
	loadavg = 0
	# iterate over hash functions
	for k in range(100):
		loadavg += fullyrandom(k, n, 100)
	Y1.append(loadavg/100.)

	load = 0
	for k in range(100):
		load += twochoice(k, n, 100)
	Y2.append(load/100.)

plt.plot(X, Y1)
plt.draw()

plt.figure()
plt.plot(X, Y2)
plt.draw()

plt.show()
		

		
