#1 Create a Python dictionary
list_of_names = ["Bob","Alice","Charlie","Delilah","Joe","Esperanza"]
list_of_majors = ["EE","CpE", "ChemE", "Journalism", "Stalking", "MechE"]

students = {
	"Name" : list_of_names,
	"Major" : list_of_majors,
	"GPA" : [1.5, 2.5, 3.8, 2.1, 4.0, 3.0]		
}

for key in students:
	#print(key)
	pass
for value in students.values():
	#print(value)
	pass

#2 Add a key to the dictionary
students["Num of absences"] = [1298, 5, 3, 1, 0, 2]

#3 Create a function to find the average GPA of all the students. 
def find_avg(GPA):
	sum = 0
	for AvgGPA in GPA:
		sum += AvgGPA
	return float(sum/len(GPA))
#print(find_avg(students["GPA"])) #my boyfriend helped me here

#4 Create a function to find the highest number absences of all the students. 
def highest(absences,N):
	max = absences[0]
	for i in range(0, N):
		if absences[i] > max:
			max = absences[i]
	return max
absences = students["Num of absences"]
N = len(absences)
ans = highest(absences,N)
#print(ans)

#5 Reset all the student’s number of absences to 0. 
students.pop("Num of absences")
for key in students:
	#print(key)
	pass
for value in students.values():
	#print(value)
	pass

#6  Say that a new student has joined this small school. 
#Append this student to the end of every list. 
#list_of_names.append("Fernando")
#list_of_majors.append("EE")
#students["GPA"].append(3.2)
#students["Num of absences"].append(0)
#for value in students.values():
	#print(value)
#	pass

# Challenge 1: Write a function that finds the maximum of a list.
def maximum(a, N): 
	max = a[0]
	for i in range(0, N):
		if a[i] > max:
			max = a[i]
	return max

#i dont know this part of the challenge:  If the list is empty, return None. 

a = [1,2,3]  
N = len(a)
#print(maximum(a, N))
pass

# Challenge 2:  Write a function that finds the minimum of a list. 
def minimum(a, N): 
	min = a[0]
	for i in range(0, N):
		if a[i] < min:
			min = a[i]
	return min

#i dont know this part of the challenge:  If the list is empty, return None. 

a = [20,50,100]  
N = len(a)
print(minimum(a, N))

# Challenge 3: Write a function that extracts all the numerical digits from a string. 
#Return these digits as a list of integers. Ifthe string is empty, or does not 
#contain any numerical digits, return an empty list. 




# Challenge 4: Write a function that takes a list as an input. 
#Find the sum between the smallest odd number and the largest odd number on that
# list. Note that the smallest odd number and largest odd number may be the
#same thing if there is only one odd number in the list.
#If there are no odd numbers, the output should be 0. 




# Challenge 5: Hacker-rank inspired Challenge – Given five positive integers, 
#find the minimum and maximum values that can be calculated by summing exactly 
#four of the five integers. Then put the respective minimum and
#maximum values into a list. Return this list. 
