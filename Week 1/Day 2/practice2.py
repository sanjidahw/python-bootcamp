import random

winning_num = random.randint(0,100)
print("The winning number is ", winning_num)

guesses = []
total_guesses = 10
user_won = False
guesses_taken = 0

while guesses_taken < total_guesses and user_won != True:
	user_guess = int(input("Enter your guess: "))
	guesses.append(user_guess)
	guesses_taken += 1

	if user_guess == winning_num:
		user_won = True
		print("Congrats, you won!")

	elif user_guess >= winning_num - 5 and user_guess <= winning_num + 5:
		print("Hot")

	elif user_guess >= winning_num - 10 and user_guess <= winning_num + 10:
		print("Warm")

	else:
		print("Cold")

print("The amount of guesses you took: ", guesses_taken)
print("Your guesses were: ")
print(guesses)