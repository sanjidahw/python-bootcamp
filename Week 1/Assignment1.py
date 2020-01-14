#Challenge #1 (⋆)
#Create a function that takes in an array (or list) of integers or floats as input. The output of the function is the sum of all the elements inside of the array. If the list is empty, the output should be 0. Print this output to console.  

def sum_up(list):
	sum= 0
	for i in range(0,len(list)):
		sum += list[i]
return sum

test=[1,2,3]
print(sum_up(test))


#Challenge #2 (⋆⋆)
#Create a function that takes an integer n as the input. The output function should be a list of all odd integers between 0 and n inclusively. If n = 0, the output list should be empty. 

def find_odds(n):
	odds = [ ] #empty list
	for num in range(0,N+1):
		if(number % 2 == 1):
			odds.append(num)
return odds

n = 19
print(find_odds(n))


#Challenge #4 (⋆⋆⋆⋆) 
#Create a function that compares two lists of integers. The output of the function should be a list containing the differences between the first and second lists. In order words, list all the elements that are unique only to ONE of the lists. If both lists are empty or the same, the output list should also be empty.  

def find_diffs(a,b):
	differences = [ ] 
	for element in a:
		if element not in b:
			differences.append(element)
	for element in b:
		if element not in a:
			differences.append(element)
return differences

test 1 = [1,2,3]
test 2 = [1,2,3]
print(find_diffs(test1,test2)	
