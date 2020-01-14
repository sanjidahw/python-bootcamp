# TODO: Make a function that takes in two inputs: A lower limit and an upper limit.
#The function should return a list of all multiples of S  between lower
# and upper limit (inclusive)

def find_mults(lower, upper):
	mults = []

	for num in range(lower, upper+1):
		if num % 5 == 0:
			mults.append(nums)
	return mults

# Test the function
print(find_mults(0,100))