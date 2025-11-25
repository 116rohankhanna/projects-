# We are going to write a program that generates a random number and asks the user to 
# guess it. 
# If the player’s guess is higher than the actual number, the program displays “Lower 
# number please”. Similarly, if the user’s guess is too low, the program prints “higher 
# number please” When the user guesses the correct number, the program displays the 
# number of guesses the player used to arrive at the number. 
# Hint: Use the random module.

from random import randint

n= randint(1,100)
gusses = 0

while True:
    a=int(input("Guess the no :- "))
    gusses+=1
    if a>n :
        print("Guess lower the no \n")
    elif a<n :
        print("Guess higher no \n")
    else:
        print(f"Your Guess is right {n} \n")
        print(f"You have guess the no {n} correctly in {gusses} attempts !")
        break
