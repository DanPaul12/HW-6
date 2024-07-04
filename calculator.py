def addition(num1, num2):
    result = num1 + num2
    print("Your answer is: " + str(result))

def subtraction(num1, num2):
    result = num1 - num2
    print(result)

def multiplication(num1, num2):
    result = num1 * num2
    print(result)

def division(num1, num2):
    result = num1 / num2
    print("Divide by zero error") if num2 == 0 else print(result)

while True:
    action = input("What operation would you like to perform? [A]ddition, [S]ubraction, [M]uliplication, or [D]ivision: ")
    if action == ("A"):
        num1 = int(input("What's your first number?: "))
        num2 = int(input("What's your second number?: "))
        addition(num1, num2)
    elif action == ("S"):
        num1 = int(input("What's your first number?: "))
        num2 = int(input("What's your second number?: "))
        subtraction(num1, num2)
    elif action == ("M"):
        num1 = int(input("What's your first number?: "))
        num2 = int(input("What's your second number?: "))
        multiplication(num1, num2)
    elif action == ("D"):
        num1 = int(input("What's your first number?: "))
        num2 = int(input("What's your second number?: "))
        division(num1, num2)
    else:
        print("Invalid input")