def addition(num1, num2):
    result = num1 + num2
    print("Your answer is: " + str(result))

def subtraction(num1, num2):
    result = num1 - num2
    print("Your answer is: " + str(result))

def multiplication(num1, num2):
    result = num1 * num2
    print("Your answer is: " + str(result))

def division(num1, num2):
    if num2 == 0:
        print("Can't divide by zero")
    else:
        result = num1 / num2
        print("Your answer is: " + str(result))

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