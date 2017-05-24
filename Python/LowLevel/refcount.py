import sys

a = [1,2,3,4]

print sys.getrefcount(a)
b = a 

print sys.getrefcount(b)


