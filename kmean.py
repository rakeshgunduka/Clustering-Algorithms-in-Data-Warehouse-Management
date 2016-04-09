import random

def kmean(ds,k):
	clusters = []
	randnums = []
	for i in range(k):
		n = random.choice(ds)
		randnums.append(n)
		ds.remove(n)
		ls = []
		ls.append(n)
		clusters.append(ls)
	print "Random Number chosen : ",randnums
	for num in ds:
		ls = []
		for rand in randnums:
			if num-rand < 0:
				ls.append(-(num-rand))
			else:
				ls.append(num-rand)
		clusters[ls.index(min(ls))].append(num)
	return clusters

if __name__ == "__main__":
	ds = [int(x) for x in raw_input("Enter Dataset [eg. 10 20 30 40...] : ").split()]
	print "Dataset provided : ",ds   									#ds = [30,35,75,65,20,10,90]
	k = int(input("Number of Clusters : "))
	clusters = kmean(ds,k)
	print "Clusters : ",clusters	
