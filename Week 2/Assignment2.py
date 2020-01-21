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

#2	Add a key to the dictionary
students["Num of absences"] = [1298, 5, 3, 1, 0, 2]

#3 Create a function to find the average GPA of all the students. 
def find_avg(GPA):
	sum = 0
	for AvgGPA in GPA:
		sum += AvgGPA
	return float(sum/len(GPA))
#print(find_avg(students["GPA"])) #my boyfriend helped me here

#4 Create a function to find the highest number absences of all the students. 


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
list_of_names.append("Fernando")
list_of_majors.append("EE")
students["GPA"].append(3.2)
students["Num of absences"].append(0)
for value in students.values():
	#print(value)
	pass