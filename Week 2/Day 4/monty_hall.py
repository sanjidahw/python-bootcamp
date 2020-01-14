import random

def organize_game():
	door_contents = [1,0,0]
	random.shuffle(door_contents)

	for i in range(0,len(door_contents)):
		if door_contents[i] == 1:
			winning_door = i

	return door_contents, winning_door

def game_time():
	door_nums = [0,1,2]
	door_contents, winning_door = organize_game()

	#we need the contestant to make a choice
	door_chosen = random.choice(door_nums)

	#now we need the game show host to open another door.
	#the game show host must open a door that does not have the 10
	#Million dollars, but the door must also not be the one that the
	#contestant picked
	unavailable_doors = [door_chosen, winning_door]
	door_to_open = set(door_nums).difference(unavailable_doors)
	door_to_open= door_to_open.pop()

	#next we need to see if the contestant won or lost
	switched_win = False
	stayed_win = False
	final_choice = 

# list1 = [1,1,1,1,1,1,5,6,7]
# print(set(list))
# list2 = [1,6,7]
#print(list1)
#print(list2)
# list3 =[]
# list1= set(list1)
# list3 = list1.difference(list2)
# print(list3)
