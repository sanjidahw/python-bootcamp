# the goal of this script is to print all the odd numbers between
# 0 and N inclusively, where N is the user input

N = int(input("Enter an upper limit: "))

#Use a for loop first
print("Using a for loop: ")
for number in range(0,N+1):
	if(number % 2 == 1):
		print(number)


#Use a while loop
print("Using a while loop: ")
counter = 1
while counter <= N:
	if(counter % 2 ==1):
		print(counter)
	counter += 1

