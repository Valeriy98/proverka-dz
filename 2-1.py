x = int(input())
y = int(input())
z = int(input())

if x == y == z:
	if x == z:
		print(3)
elif x == y or y == z or z == x: 
	print(2)
else: 
	x != y != z
	x != z
	print(0)