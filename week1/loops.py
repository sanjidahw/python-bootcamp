counter = 0

while counter <= 10:
	print(counter)
	counter += 1

# range(start, stop, increment)
# includes the start, does not include the stopping number
print("using the inputs to range()")
for number in range(0,5,1):
	print(number)

print("using one input to range()")
for number in range(5):
	print(number)
