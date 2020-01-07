# practing with lists and functions

#Example: define a function that returns a list of even 
#numbers between A and B (inclusive)

def find_evens(A,B):
	evens = []
	for nums in range(A,B+1):
		if(nums % 2 == 0):
			evens.append(nums)
	return evens
#print(find_evens(2,20))

#TODO: Define a function that returns a list of numbers between 
#A and B (inclusive) that are even multiples of 3
def even_multiples(A,B):
	multiples = []
	for num in range(A,B+1):
		if (num % 6 == 0):
		#if (num % 3 == 0) and (num % 2 == 0):
			multiples.append(num)
	return multiples
print(even_multiples(0,20))
