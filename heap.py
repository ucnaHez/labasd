#!/usr/bin/python
hsize = 0
heap = []
f = open("4.in", 'r')
aminp = f.readline()
inp = f.readlines()
#print inp

def hadd(h, n):
	h.append(n)
	hrestoreup(h,len(h)-1)

def hremove(h):
	ret = h[0]
	h[0] = h[-1]
	del h[-1]
	hrestoredown(h, 0)
	return ret

def hrestoreup(h, ind):
	if ind <= 0:
		return
	if h[ind] > h[(ind-1)/2]:
		t = h[(ind-1)/2]
		h[(ind-1)/2] = h[ind]
		h[ind] = t
		hrestoreup(h,(ind-1)/2)
	return

def hrestoredown(h,ind):
	if (ind*2 + 2) > len(h)-1:
		return
	if h[ind*2 + 2] > h[ind*2 + 1]:
		var = 2
	else:
		var = 1
	if h[ind] < h[ind*2 + var]:
		t = h[ind]
		h[ind] = h[ind*2 + var]
		h[ind*2 + var] = t
		hrestoredown(h, ind * 2 + var)
	return
			
		
for i_r in inp:
	i = i_r.strip("\n")
	if i == "GET":
		r = hremove(heap)
		print r
	else:
		hadd(heap, int(i))
#	print heap

		