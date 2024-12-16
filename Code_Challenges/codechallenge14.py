sum = 0
while True:
    user_input = input("Enter a number --> ")
    if user_input == "0":
        break  
    
    sum += eval(user_input)  
print("The sum of all the numbers given is", sum)
