import random


number_to_guess = random.randint(1, 100) #computer set random number
tries = 0
print("Wellcome to Guess a Number mini game. Try to guess a random number between 1 and 100 in 10 tries")

while tries < 10:
    players_guess = input("Guess the number from 1 to 100: ") #read player's guess

    if int(players_guess) not in range(1, 101): #check player's guess for range of input
        print("Your number is out of range.")
        continue

    elif not players_guess.isdigit(): #check player's guess for type of input
        print("Invalid input! Try again...")
        continue

    players_guess = int(players_guess)

    if players_guess == number_to_guess:
        print("You guess it and won the game")
        break

    elif players_guess > number_to_guess:
        print("Your number is higher!")

    elif players_guess < number_to_guess:
        print("Your number is lower!")

    tries += 1

else:
    print("Sorry, no more tries. You lost")