def search(x, list):
	for index in range(0,len(list)):
		if list[index] == x:
			return index

	this_list = [10, 9, 8, 7, 6, 5]
	ans = search(2,this_list)
	print(ans)
