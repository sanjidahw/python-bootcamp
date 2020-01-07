# the goal of this script is to sum up all the numbers between
# N and M (inclusively), where N and M are both user inputs

N = int(input("Enter an lower limit: "))
M = int(input("Enter an upper limit: "))

#Use a for loop
print("Using a for loop: ")
sum = 0
for number in range(N,M+1):
	sum += number
	# sum = sum + number
	print("The total sum is: ", sum)
	# print("the type is: ", type(sum))


#Use a while loop
print("\nUsing a while loop: ")
sum = 0
number = N
while number <= M:
	sum += number
	number += 1
print("The total sum is: ", sum)