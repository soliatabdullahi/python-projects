import random
number_to_guess = random.randint(1,100)
username = input("Username:")
attempts = 5
while attempts > 0 :
    print(f"{username.title()} You have {attempts-0} attempt!\n")
    try:
        guess = int(input("Enter a number_between 1-100:"))
        if guess < number_to_guess:
            print("Too low!\n")

        elif guess > number_to_guess:
            print("Too high!\n")
        else:
            print("Congratulation! you guessed the number.")
            break
        attempts -= 1
        if attempts == 0:
            print(f"Game over! the number is {number_to_guess}") 
    except ValueError:
        print(f"Focus {username.title()}! enter a valid number please!\n")




