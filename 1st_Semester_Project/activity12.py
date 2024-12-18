def forloop_ex2():
    n1 = 0
    odd = 0  
    even = 0 

    for i in range(1, 10):
        try:
            n2 = int(input(f"Enter a number {i}: "))  
            n1 += n2  
            if n2 % 2 == 0:
                even += n2  
            else:
                odd += n2  
        except ValueError:
            print("Please enter a valid integer.")  

    print(f"The total of all the numbers you entered is {n1}")
    print(f"The total of the odd numbers you entered is {odd}")
    print(f"The total of the even numbers you entered is {even}")

