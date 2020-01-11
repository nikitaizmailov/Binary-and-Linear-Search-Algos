# Practise try without looking! binary search and linear search models
# Both are iterative methods

# Binary search algorithm is faster and more efficient

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
searched_number = 0

def binSearch(array, number):

	lower_b = 0
	upper_b = len(array) - 1

	while lower_b <= upper_b:

		mid_pos = (lower_b + upper_b) // 2

		if array[mid_pos] == number:
			return mid_pos
		else:
			if array[mid_pos] < number:
				lower_b = mid_pos + 1
			else:
				upper_b = mid_pos - 1

	return None

test1 = binSearch(list1, searched_number)

if test1 is not None:
	print("The number's position is ", test1 + 1)
else:
	print("Position not found")

# Linear search algortihm Iterative!!!

def linSearch(array, number):

	for i in range(len(array)):
		if array[i] == number:
			return i
		else:
			pass

	return None

test2 = linSearch(list1, searched_number)

if test2 is not None:
	print("The number's position is ", test2 + 1)
else:
	print("Position not found")
