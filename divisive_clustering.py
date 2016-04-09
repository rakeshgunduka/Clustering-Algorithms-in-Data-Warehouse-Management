import random,copy
inc = 20
j = 10
q = 0
p = 10
def kmean(ds,k,j,q):
	clusters = []
	randnums = []
	ads = copy.copy(ds)
	if q != 0:
		print " "*(q-k),"|"
		print " "*(q-k),"|","-"*p,ads
	if len(ds) == 1:
		return
	for i in range(k):
		n = random.choice(ds)
		randnums.append(n)
		ds.remove(n)
		ls = []
		ls.append(n)
		clusters.append(ls)
	for num in ds:
		ls = []
		for rand in randnums:
			if num-rand < 0:
				ls.append(-(num-rand))
			else:
				ls.append(num-rand)
		clusters[ls.index(min(ls))].append(num)
	q = j
	j += inc
	for i in clusters:
		kmean(i,2,j,q)

def divisive(ds):
	print "\nDendogram for Given Dataset :"
	print ds
	kmean(ds,2,j,q)
	print

if __name__ == "__main__":
	ds = [int(x) for x in raw_input("Enter Dataset [eg. 10 20 30 40...] : ").split()]
	#ds = [50,15,95,5,100,55,30,75]
	print "Dataset provided : ",ds   							
	divisive(ds)	
