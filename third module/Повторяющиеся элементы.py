
l = [1, 4, 1, 6, "hello", "a", "5", "hello"]
l_ne = []
for i in l:
	if i not in l_ne:
		l_ne.append(i)
print(l_ne)