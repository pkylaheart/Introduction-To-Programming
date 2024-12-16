number1 = eval(input("Enter the first number: "))
number2 = eval(input("Enter the second number: "))

sum_result = number1 + number2
difference = number1 - number2
product = number1 * number2
quotient = number1 / number2 if number2 != 0 else "undefined (division by zero)"
modulus = number1 % number2 if number2 != 0 else "undefined (modulus by zero)"
exponentiation = number1 ** number2

print(f"The sum of {number1} and {number2} is: {sum_result}")
print(f"The difference between {number1} and {number2} is: {difference}")
print(f"The product of {number1} and {number2} is: {product}")
print(f"The quotient of {number1} divided by {number2} is: {quotient}")
print(f"The modulus of {number1} and {number2} is: {modulus}")
print(f"The result of {number1} raised to the power of {number2} is: {exponentiation}")
