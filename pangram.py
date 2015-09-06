import sys
T = sys.stdin.readline()
z= sorted(list(T.upper().strip().replace(" ","")))
y=set(z)
if len(y)==26:
    print 'pangram'
else:
    print 'not pangram'
