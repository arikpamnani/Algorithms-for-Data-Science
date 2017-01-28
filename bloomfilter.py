import math
def hash(a, x, p):
	return (a*x) % p

class BloomFilter:
	def __init__(self, n, m):
		self.BF = [False] * m	# bit-array
		self.n = n
		self.m = m
		self.k = int(math.ceil(0.685 * float(m) / float(n)))
			
	def insert(self, x):		
		for i in range(1, self.k + 1):
			# j = hash(i, x, p) % self.m
			j = (i*x) % self.m;
			self.BF[j] = True
		
	def lookup(self, x):
		for i in range(1, self.k + 1):
			j = (i*x) % self.m
			if(not self.BF[j]):
				return False
		return True
		
if __name__ == "__main__":
	n, m = map(int, raw_input().split())
	BF = BloomFilter(n, m)
	# test -> insert + lookup
	while(True):
		x = raw_input()
		if(x == 'q'):
			break
		elif(x.split()[0] == 'i'):
			BF.insert(int(x.split()[1]))
		else:
			print BF.lookup(int(x.split()[1]))
	
	
