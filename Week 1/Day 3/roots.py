#finding the roots of a function between a specific region

def f(x):
	return 2*x + 1

def find_root(a,b):
	c = (a+b)/2 #initial c
	ans = f(c) #f(c)
	num_iterations = 0
	
	while ans != 0 and num_iterations <= 1000:
		num_iterations += 1
		c = (a+b)/2
		ans = f(c) 
	
		if (ans > 0):
			b = c

		elif (ans < 0):
			a = c

	if(num_iterations == 1000 and f(c) != 0):
		print("There is no zero in this region")
		return None
	else:
		return c
print(find_root(lower,upper))


# For sinusoids
def f(x):
	return math.cos(x)

def find_root(a,b):
	c = (a+b)/2 #initial c
	ans = f(c) #f(c)
	num_iterations = 0
	tolerance = 0.01
	
	while ans != 0 and num_iterations <= 1000 and ans > tolerance:
		num_iterations += 1
		c = (a+b)/2
		ans = f(c) 
	
		if (ans > 0):
			b = c

		elif (ans < 0):
			a = c

	if(num_iterations == 1000 and f(c) != 0 and ans>tolerance):
		print("There is no zero in this region with that tolerance")
		return None
	else:
		return c

lower = math.pi
upper = 2*math.pi

print(find_root(lower,upper))
print(3*math.pi/2)