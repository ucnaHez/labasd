#!/usr/bin/python
f = open("5.in", 'r')
size = int(f.readline())
inp = f.readline()
inpsplit = inp.split(" ")
arr = []
for i in inpsplit:
	arr.append(int(i))
searchsize = f.readline()
searchinp = f.readlines()
arrtosearch = []
for i in searchinp:
	arrtosearch.append(int(i))
f.close()

for tosearch in arrtosearch:
#	print "finding ",
#	print tosearch
	left = 0
	right = size
	while 1:
		if tosearch == arr[(right + left) / 2]:
#			print "Found, ", str((right+left)/2)
			print str((right+left)/2)
			break
		elif abs(right - left) == 1:
#			print "not found, boundaries connected"
			print -1
			break
		elif tosearch > arr[(right + left) / 2]:
			left = (right + left) / 2
#			print "leftmoving, ", left, " right is: ", right
		elif tosearch < arr[(right + left) / 2]:
			right = (right + left) / 2
#			print "rightmoving, ", right, " left is: ", left
		else:
#			print "not found, elsewhere"
			print -1
			break
