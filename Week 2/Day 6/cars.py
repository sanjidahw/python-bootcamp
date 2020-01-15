def find_avg(years):
	sum = 0
	for year in years:
		sum += year
	return int(sum/len(years))
#or 
#def find_avg2(years):
#	return int(sum(years)/len(years))

list_of_cars = ["Toyota","Ford","B&W","Audi","Benz"]
list_of_models = ["Camry","F150", "i8", "A4", "S550"]

car = {
	"make" : list_of_cars,
	"model" : list_of_models,
	"years" : [2018, 2017, 2016, 2015, 2014]		
}

for key in car:
	#print(key)
	pass

car_years = car["years"]
#print(car_years)

#Challenge: Find the average years the cars were produced
avg_year = find_avg(car_years)
#print(f"The average year of all the cars are: {avg_year} ")

car_colors = ["red", "blue", "yellow", "green", "black"]
car["color"] = car_colors

for key in car:
	#print(key)
	pass
for value in car.values():
	#print(value)
	pass

car["Number in Stock"] = [3, 5, 6, 1, 3]

for key in car:
	#print(key)
	pass
#Print all the values stored in this dictionary
for value in car.values():
	#print(value)
	pass

#Challenge: Tell me how many cars we have in stock by accessing
#the "Number in Stock" key from dictionary
inventory = car["Number in Stock"]
#print(f"We have {sum(inventory)} cars in stock.")


car["Dealers"] = ["Amy", "Bob", "Charlie", "Dylan", "Elephant"]

for key in car:
	#print(key)
	pass
for value in car.values():
	#print(value)
	pass

#Remove the label
#print("Firing all the dealers...")
#car.pop("Dealers")
#for key in car:
#	print(key)
#   or use
#car["Dealers"].clear()

print(car)
print("\n we're going to close our dealership")
car.clear() #erase the contents of the dictionary
print(car)
del car #delete the whole dictionary
#print(car)