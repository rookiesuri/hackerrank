def tree(n):
	if n==0:
		print 1
	else:
		sum1 =1
		for x in range(1,n+1):
			if x%2 ==1:
				sum1=sum1*2
			else:
				sum1=sum1+1
		print sum1
        
import sys
T = int(sys.stdin.readline())
for _ in range(T):
     N = int(sys.stdin.readline())
     tree(N)

