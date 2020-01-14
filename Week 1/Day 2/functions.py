# define f(x) = x + 1
def f(x):
	ans = x + 1
	return ans
my_solution1 = f(1)
print(my_solution1)


#define a function of x, where g(x) = x^4 + x^2 + 1
def g(x):
	ans = x**4 + x**2 + 1
	return ans
print(g(1), g(2), g(3))


#function with multiple returns
def get_first_two_evens():
	return 2, 4
even1, even2 = get_first_two_evens()
print(even1)
print(even2)


#function with no returns
def print_even(N):
	for num in range(0,N+1):
		if num % 2 == 0:
			print(num)
print_even(10) #should print 2,4,6,8,10

#To-do: write a function that takes N as a input and prints all common
#multiples of 3 and 7, between 0 and N (inclusive)
def my_function(N):
	for num in range(0,N+1):
		if (num % 3 == 0) and (num % 7 == 0):
			print(num)
my_function(100)

#define a function that takes 3 inputs: x, y, N the function 
#will find all the common multiples of x and y between 0 and N
def more_functions(x,y,N):
	for num in range(0,N):
		if (num % x == 0) and (num % y == 0):
			print(num)
more_functions(3,7,100)