print("Welcome to Calculator!\n")

print("1. Add \n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")


try:
    op = int(input("Choose opreation: "))
    if op <= 0 or op > 5:
        print("Please enter an opreation from the given!\n")
except ValueError:
    print("Please enter a number!\n")
    

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Please enter a number!\n")

def add(num1, num2):
    return num1+num2
    
def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1/num2

if op == 1:
    print(add(num1, num2))
elif op == 2:
    print(sub(num1, num2))
elif op == 3:
    print(mul(num1, num2))
elif op == 4:
    print(div(num1, num2))
elif op == 5:
    print("Goodbye!")
    break
