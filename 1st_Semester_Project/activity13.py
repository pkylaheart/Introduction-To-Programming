def forloop_ex3():
    while True:
        try:
            num = input("Enter a number: ")

            num = int(num)  
            if num > 100:
                print("Number is too large. Please enter a number less than or equal to 100.")
                continue 
            fac = 1
            for i in range(num, 1, -1):
                fac *= i

            print(f"The factorial of {num} is {fac:,}") 
            break  
        except ValueError:
            print("Please enter a valid integer.")  