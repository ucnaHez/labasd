#!/usr/bin/python
f = open("5.in", 'r')
size = int(f.readline())
amount = int(f.readline())
inp = f.readlines()
arr = []
for i in inp:
	arr.append(int(i))

f.close()

def check2(leng, am, arr):
	coun = 0
	i = 0
	while i < len(arr):
		jump = arr[i] + leng
		coun += 1
		if jump >= arr[-1]:
			break
		for n in range(len(arr)):
			if arr[n] > jump:
				i = n
				break
	if am >= coun:
		return 1
	else:
		return 0

left = 0
right = arr[-1] - arr[0]
while 1:
	if abs(right - left) == 1:
#		print "boundaries connected"
#		print "lasttrue: ", lasttrue
		print lasttrue
		break
	elif not check2((right + left) / 2, amount, arr):
		left = (right + left) / 2
#		print "leftmoving, ", left, " right is: ", right
	elif check2((right + left) / 2, amount, arr):
		lasttrue = (right+left)/2
		right = (right + left) / 2
#		print "rightmoving, ", right, " left is: ", left
	else:
#		print "not found, elsewhere"
		print -1
		break
