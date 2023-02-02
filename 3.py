#x = float(input())
#y = float(input())
#if x > y:
#	print(x)
#else: 
#	if x < y:
#		print(y)



x = int(input())
y = int(input())

maxi = (x >= y) * x or (y >= x) * y
print(maxi)