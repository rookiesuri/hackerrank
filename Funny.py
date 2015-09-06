# Enter your code here. Read input from STDIN. Print output to STDOUT

def diff_asci(c1,c2):
	z=abs(ord(c1)-ord(c2))
	return z




def compare(arr):
	arr2=[]
	result='Funny'
	for i in reversed(arr):
		arr2.append(i)
	for i in range(0,len(arr)-1):
		if diff_asci(arr[i],arr[i+1])!=diff_asci(arr2[i],arr2[i+1]):
			result='Not Funny'
			break
	print result

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = sys.stdin.readline()
    compare(list(N.strip()))
	
