winning_number = random.randint(0,10)
print(winning_number)

num_guesses = 5
user_won = False

while num_guesses != 0 and user_won == False:
	user_guess = int(input("Enter your guess: "))
	if user_guess == winning_number:
		print("You won")
		user_won = True
	else:
		num_guesses -= 1
		if num_guesses == 0:
			print("You lost")
		else:
			print("Try again")

