def calculator():    
    sum_result = number1 + number2
    difference = number1 - number2
    product = number1 * number2
    quotient = number1 / number2 if number2 != 0 else "undefined (division by zero)"
    modulus = number1 % number2 if number2 != 0 else "undefined (modulus by zero)"
    exponentiation = number1 ** number2

    if choice == '1':
        number1 = eval(input("Enter the first number: "))
        number2 = eval(input("Enter the second number: "))
        print(f"The sum of {number1} and {number2} is: {sum_result}")
    elif choice == '2':
        number1 = eval(input("Enter the first number: "))
        number2 = eval(input("Enter the second number: "))    
        print(f"The difference between {number1} and {number2} is: {difference}")
    elif choice == '3':
        number1 = eval(input("Enter the first number: "))
        number2 = eval(input("Enter the second number: "))
        print(f"The product of {number1} and {number2} is: {product}")
    elif choice == '4':
        number1 = eval(input("Enter the first number: "))
        number2 = eval(input("Enter the second number: "))
        print(f"The quotient of {number1} divided by {number2} is: {quotient}")
    elif choice == '5':
        number1 = eval(input("Enter the first number: "))
        number2 = eval(input("Enter the second number: "))
        print(f"The modulus of {number1} and {number2} is: {modulus}")
    elif choice == '6':
        number1 = eval(input("Enter the first number: "))
        number2 = eval(input("Enter the second number: "))
        print(f"The result of {number1} raised to the power of {number2} is: {exponentiation}")


    

    