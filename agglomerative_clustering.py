import random,copy
flag = 0
step = 0
clusters = []
	
def merge_col(col_set,dds,dmat):
	mat = copy.copy(dmat)
	ds = copy.copy(dds)
	vt = [0,0]
	for i,val in enumerate(ds):
		if mat[i][col_set[0]]>mat[i][col_set[1]]:
			vt[0] += 1
		else:
			vt[1] += 1
	replace_to = ds[col_set[vt.index(min(vt))]]
	for i,j in enumerate(vt):
		if i != vt.index(min(vt)):
			#print i
			ti = col_set[i]

	delete = ds[ti]
	del mat[ti]
	for i,j in enumerate(mat):
		del mat[i][ti]
	ds[col_set[vt.index(min(vt))]] = str(ds[col_set[vt.index(min(vt))]]+"+"+ds[ti])
	del ds[ti]
	return ds,mat

def agglomerative(ds,mat):
	global step
	ls = []
	step += 1
	print "Step:",step,"-->",
	for data in ds:
		print data,"\t",
	print
	if len(mat) == 1:
		return
	clusters.append(ds)
	for index,i in enumerate(mat):
		ls.append(min(i))
	tmp_ls = []
	tmp_ls.append(ls.index(min(ls)))
	tmp_ls.append(mat[ls.index(min(ls))].index(min(ls)))
	ds,mat = merge_col(tmp_ls,ds,mat)
	agglomerative(ds,mat)

if __name__ == "__main__":
	ds = [int(x) for x in raw_input("Enter Dataset [eg. 10 20 30 40...] : ").split()]
	#ds = [50,15,95,5,100,55,30,75]
	inf = float("inf")
	print "Dataset provided : ",ds   							
	mat = []
	for m,i in enumerate(ds):
		ls = []
		for n,j in enumerate(ds):
			if j-i < 0:
				ls.append(-(j-i))
			elif j-i > 0:
				ls.append(j-i)
			else:
				ls.append(inf)
		mat.append(ls)
	for i,j in enumerate(ds):
		ds[i] = str(ds[i])
	agglomerative(ds,mat)
