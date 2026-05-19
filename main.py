def add(num1, num2):
    return num1+num2
        
def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Cannot divide by zero!"



while True:
    print("\nWelcome to Calculator!\n")
    
    print("1. Add \n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    
    
    while True:
        try:
            op = int(input("Choose opreation: "))
            if op <= 0 or op > 5:
                print("Please enter an opreation from the given!\n")
            else:
                break
        except ValueError:
            print("Please enter a number!\n")
        
        
    if op == 5:
        print("\nGoodbye!")
        break
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Please enter a number!\n")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Please enter a number!\n")
        
        

    if op == 1:
        print(f"Answer: {add(num1, num2)}")
    elif op == 2:
        print(f"Answer: {sub(num1, num2)}")
    elif op == 3:
        print(f"Answer: {mul(num1, num2)}")
    elif op == 4:
        print(f"Answer: {div(num1, num2)}")
    
