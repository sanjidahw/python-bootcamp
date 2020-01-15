#Example of a dictionary

my_personal_info = {
	"Name" : "Sanji",
	"DOB" : "08/26/1998",
	"School" : "CCNY",
	"GPA" : 4.0
}

#Dictionaries are known for their "key-value" pair system

#Checking if a key exists in a dictionary
if "Name" in my_personal_info:
	#print(my_personal_info["name"])
	pass
else:
	#print("It's not in the dictionary")
	pass

#Print out all the keys in the dictionary
for key in my_personal_info:
	print(key)
	pass

#Print out all the values in the dictionary (without the key)
for value in my_personal_info:
	print(value)
	pass