import random


print("Wellcome to Guess a Number mini game. Try to guess a random number between 1 and 100 in 10 tries")

number_limit_based_on_difficulty = 0
tries = 0
tries_count = 0

while True: #user can choose difficulty of the game
    print("Choose difficulty")
    print("Easy: 10 tries and number range 1 - 100")
    print("Medium: 10 tries and number range 1 - 500")
    print("Hard: 10 tries and number range 1 - 1000")
    difficulty = input("Please select Easy, Medium or Hard: ")

    if difficulty == "Easy":
        number_limit_based_on_difficulty = 100
        break
    elif difficulty == "Medium":
        number_limit_based_on_difficulty = 500
        break
    elif difficulty == "Hard":
        number_limit_based_on_difficulty = 1000
        break
    else:
        print("Invalid selection. Try again...")

while True: #user can choose number of tries
    how_many_tries = input("How many tries you want?: ")
    if how_many_tries.isdigit() and int(how_many_tries) > 0:
        tries = int(how_many_tries)
        break
    else:
        print("Invalid input. Try again...")


number_to_guess = random.randint(1, number_limit_based_on_difficulty) #computer set random number


while tries_count < tries:
    players_guess = input(f"Guess the number from 1 to {number_limit_based_on_difficulty}: ") #read player's guess

    if int(players_guess) not in range(1, number_limit_based_on_difficulty + 1): #check player's guess for range of input
        print("Your number is out of range.")
        continue

    elif not players_guess.isdigit(): #check player's guess for type of input
        print("Invalid input! Try again...")
        continue

    players_guess = int(players_guess)

    if players_guess == number_to_guess:
        print("You guess it and won the game!")
        break

    elif players_guess > number_to_guess:
        print("Your number is higher!")

    elif players_guess < number_to_guess:
        print("Your number is lower!")

    tries_count += 1

else:
    print("Sorry, no more tries. You lost")