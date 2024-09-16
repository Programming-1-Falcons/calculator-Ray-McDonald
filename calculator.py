while True:
    operation = input("What mathmatical operation?: ")
    num1 = float(input("What is the first number?: "))
    num2 = float(input("What is the second number?: "))

    if operation == "/" and num2 == 0:
        print("You cannot divide by zero. Try again")
    #addition
    if operation == "+":
        print(num1, operation, num2, "=", round(num1 + num2, 3))
    #subtraction
    elif operation == "-":
        print(num1, operation, num2, "=", round(num1 - num2, 3))
    #division (floating point)
    elif operation == "/":
        print(num1, operation, num2, "=", round(num1 / num2, 3))
    #multiplication
    elif operation == "*":
        print(num1, operation, num2, "=", round(num1 * num2, 3))
    #exponents
    elif operation == "**":
        print(num1, operation, num2, "=", round(num1 ** num2, 3))
    else:
        print("Invalid input. Did you enter a number and operation sign correctly?")
    

#*** bonus points:

#get a number of floating point digits to round the answer to

#handle user input issues like non numbers and/or if the user puts in a zero for the denominator on division.

#add roots or other additional mathematical processes.

#do something else creative with this calculator
