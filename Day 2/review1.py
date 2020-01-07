#To-do: write a script that prints out the the multiple of 3 between
#0 and N (inclusively), where N is an user input

#Using a for loop

N = int(input("Enter the upper limit: "))

for num in range(0,N+1):
	if num % 3 == 0:
		print(num)

#Using a while loop

counter = 0
while counter <= N:
	if counter == 0:
		print(counter)
	counter += 1

