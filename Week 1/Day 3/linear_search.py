#TODO: Write a function that takes an integer and a list as the input
#the function should return the index of where the integer was found on the list

def search(x, list):
	"""
	this function returns the index of where the element x was found on the list,
	"""
	for index in range(0,len(list)):
		if list[index] == x:
			return index

	my_list = [10, 8, 7, 19, 42, 2]
	ans = search(2,my_list)
	print(ans)

def find_max(list):
	"""
	this function returns the maximum element in the list.
	/tparam : list  - a list of numerical elements
	/treturns : the maximum value in the list
	"""
	max = list[0]
	for i in range(0,len(list)):
		if list[i] >= max:
			max = list[i]
	return max
	my_list = [10, 8, 7, 19, 42, 2]
	print(find_max(my_list))

	#for element in list:
	#	if element >= max:
	#		max = element
	#return max