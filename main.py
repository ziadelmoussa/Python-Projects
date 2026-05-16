import random

print("Welcome to the Number Guessing Game!\n")

print("Choose difficulty: ")

easy_mode = print("1. Easy - 10 attempts")
medium_mode = print("2. Medium - 7 attempts")
hard_mode = print("3. Hard - 5 attempts\n")

mode = int(input("Type number of difficulty: "))

def number_generator():
    global random_num
    random_num = random.randint(1,100)
    print(random_num)
    print("I picked a number between 1 and 100.\n")
    
def number_of_trys(number):
    for i in range(number):
        picked_number = int(input("Enter your number: "))
        if picked_number == random_num:
            print(f"\nCorrect! You guessed it in {i+1} attempts." )
            return True
        elif picked_number > random_num:
            print("Too high!")
        elif picked_number < random_num:
            print("Too low!")
    return False
            
def no_more_trys():
    print("\nYou lost! You ran out of attempts")
    print(f"The correct number was {random_num}.")
        
        

if mode == 1:
    print("Easy difficulty - 10 attempts\n")
    number_generator()
    won = number_of_trys(10)
    if not won:
        no_more_trys()
    
elif mode == 2:
    print("Medium difficulty - 7 attempts\n")
    number_generator()
    won = number_of_trys(7)
    if not won:
        no_more_trys()
    
elif mode == 3:
    print("Hard difficulty - 5 attempts\n")
    number_generator()
    won = number_of_trys(5)
    
    if not won:
        no_more_trys()
    
else:
    print("Enter a valid number")



    


    

