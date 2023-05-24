a = [1, 2, 3, 4, 5, 6, 7, 15 ,65 ,108,205]
def binaty_search(alph_array, item):
	first_pos = 0
	last_pos = len(alph_array) - 1

	while first_pos <= last_pos:
		center_value = (first_pos + last_pos) // 2
		if alph_array[center_value] == item:
			return alph_array.index(alph_array[center_value])
		else:
			if item < alph_array[center_value]:
				last_pos = center_value - 1
			else:
				first_pos = center_value + 1
	return False

print(binaty_search(a, 5))