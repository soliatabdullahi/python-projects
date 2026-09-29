# i import random as to give me numbers randomly without repetition in a run
import random
number_to_guess = random.randint(1,100)
# it asks users for name as a recognition
username = input("Username:")
# i set the guessing game to 5 attempts to make it fun and challenging
attempts = 5
# i used while loop because i want the game to keep running as long as attempt is not 0
while attempts > 0 :
# I used this print to remind users on how many attempts they have left
    print(f"{username.title()} You have {attempts-0} attempt!\n")
# I used try keyword to handle potential errors safely and prevent the program from crashing 
    try:
# I set guess as int input for users to enter guess number
        guess = int(input("Enter a number_between 1-100:"))
# here are conditions to run
        if guess < number_to_guess:
            print("Too low!\n")

        elif guess > number_to_guess:
            print("Too high!\n")
        else:
            print("Congratulation! you guessed the number.")
 # i used break keyword to stop the loop  
            break
#i set the attempt to keep subtracting until the condition is met 
        attempts -= 1
# i set this to stop attempts immediately it gets to 0 and print game over 
        if attempts == 0:
            print(f"Game over! the number is {number_to_guess}") 
#I use except ValueError to handle invalid user input. 
    except ValueError:
        print(f"Focus {username.title()}! enter a valid number please!\n")




