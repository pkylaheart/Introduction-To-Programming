product = 1  
num = eval(input("Enter a number: "))

for i in range(10, 0, -1):
    product *= num * i  
print(f"The product is: {product}")
