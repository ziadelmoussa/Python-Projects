import random

print("Welcome to the Number Guessing Game!")

print("Choose difficulty: ")

easy_mode = print("1. Easy - 10 attempts")
medium_mode = print("2. Medium - 7 attempts")
hard_mode = print("3. Hard - 5 attempts")

mode = int(input("Type number of difficulty: "))

def number_generator():
    global random_num
    random_num = random.randint(1,100)
    return random_num
    
def number_of_trys(number):
    for i in range(number):
        picked_number = int(input("Enter your number from 1 - 100: "))
        if picked_number == random_num:
            print(f"Correct! You guessed it in {i+1} attempts." )
            break
        elif picked_number > random_num:
            print("Too high!")
        elif picked_number < random_num:
            print("Too low!")
        

if mode == 1:
    print("Easy difficulty - 10 attempts")
    number_generator()
    number_of_trys(10)
    
elif mode == 2:
    print("Medium difficulty - 7 attempts")
    number_generator()
    number_of_trys(7)
    
elif mode == 3:
    print("Hard difficulty - 5 attempts")
    number_generator()
    number_of_trys(5)
else:
    print("Enter a valid number")
