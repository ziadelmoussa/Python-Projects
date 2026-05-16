print("Welcome to the Number Guessing Game!")

print("Choose difficulty: ")

easy_mode = print("1. Easy - 10 attempts")
medium_mode = print("2. Medium - 7 attempts")
hard_mode = print("3. Hard - 5 attempts")

mode = int(input("Type number of difficulty: "))

if mode == 1:
    print("Easy difficulty - 10 attempts")
    
elif mode == 2:
    print("Medium difficulty - 7 attempts")

elif mode == 3:
    print("Hard difficulty - 5 attempts")

else:
    print("Enter a valid number")
