#!/usr/bin/python
bstsize = 0
f = open("1.in", 'r')
aminp = f.readline()
inp = f.readlines()
#print inp

#import sys
#print(sys.getrecursionlimit())
#sys.setrecursionlimit(100000)


class bstnode:
	def __init__(self, par):
		self.num = None
		self.parent = par
		self.left = None
		self.right = None


def bstadd(b, n):
	if b.num == None:
		b.num = n
		print "-",
		return b
	elif b.num > n:
		if b.left == None:
			b.left = bstnode(b)
		return bstadd(b.left, n)
	elif b.num < n:
		if b.right == None:
			b.right = bstnode(b)
		return bstadd(b.right, n)
	else:
		print "+",
		return b


def bstnext(b):
	if b.right != None:
		return bstmin(b.right)
	else:
		par = b
		while 1:
			if par == None:
				return None
			grandpar = par.parent
			if grandpar == None:
				return None
			if grandpar.left == par:
				return grandpar
			else:
				par = grandpar

def bstmin(b):
	if b.left == None:
		return b
	else:
		return bstmin(b.left)

bst = bstnode(None)
for i in inp:
#	print int(i)
	added = bstadd(bst, int(i))
	q = bstnext(added)
	if q:
		print q.num
	else:
		print "-"

