def activity3():
    print("\t\t\t\t\t\t\t\tBIO-DATA")

    name = input("Name: ") 
    age = input("Age: ")
    gender = input("Gender: ")
    nationality = input("Nationality: ")
    father_name = input("Father's Name: ")
    mother_name = input("Mother's Name: ")
    dob = input("Date of Birth: ")
    pob = input("Place of Birth: ")
    civil_status = input("Civil Status: ")
    occupation = input("Occupation: ")
    address = input("Address: ")
    contact_num = input("Contact Number: ")
    email = input("Email: ")

    print("\n\n\t\t\t\t\t\t\tThank you for answering! :) \n\n\n=================================================================================================================================================\n=================================================================================================================================================")

    print("\n\n\n\t\t\t\t\t\t\t Personal Information" + "\n\nHi, My name is " + name + ", " "I'm a " + gender + " and I'm " + age + " years old." + " I was born on " + dob + " in " + pob + "." + " My nationality is " + nationality + ". My father's name is " + father_name + " and my mother's name is " + mother_name + " My occupation is being a " + occupation + " and my civil status is " + civil_status + "." + "\n\n\t\t\t\t\t\t\t Contact Information" + "\n\nI currently live in " + address + ". If needed feel free to contact me at this number " + contact_num + " or through this email " + email + ".")
        
def activity4():
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

        
def activity6():
    #This is a comment

    x = 5

    print(x)

    x = x + 5

    print(x)

    x = x + 20

    print(x)

    x += 30

    print(x)
            
tryAgain = ""
while True:
    if tryAgain.lower() == "no":
        break
    choose = input(" Choose activity you want to execute: \n A = Activity 3\n B = Activity 4\n C = Activity 6\n ")
    if choose.lower() == "a":
        activity3()
    elif choose.lower() == "b":
        activity4()
    elif choose.lower() == "c":
        activity6()
    else:
        print(" Invalid input, try again: ")
        continue
    print()
    while True:
        tryAgain = input(" Do you want to try again? yes / no\n ")
        if tryAgain.lower() == "yes":
            break
        elif tryAgain.lower() == "no":
            break
        else:
            print(" Invalid answer, try again")
            continue

print(" Program Terminated.")