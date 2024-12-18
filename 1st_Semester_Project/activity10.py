import os

def clear_screen():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def identification():
    # DLL YEAR LEVEL IDENTIFICATION

    name = input("Enter your name: ")
    
    while True:
        isStudent = input("Are you a current student of DLL (yes / no): ").lower()

        if isStudent == "yes":
            while True:
                yearLevel = input("What year are you currently enrolled in? \nF - Freshmen\nS - Sophomore\nJ - Junior\nSN - Senior\n").lower()
                
               
                if yearLevel == "f":
                    print(f"Hi {name}, Freshman, welcome to DLL")
                    break  
                elif yearLevel == "s":
                    print(f"Hi {name}, Sophomore, welcome to DLL")
                    break  
                elif yearLevel == "j":
                    print(f"Hi {name}, Junior, welcome to DLL")
                    break  
                elif yearLevel == "sn":
                    print(f"Hi {name}, Senior, welcome to DLL")
                    break  
                else:
                    print("Invalid input. Please enter a valid year level: F, S, J, or SN.")
                    clear_screen()
                    continue  

            break  

        elif isStudent.strip() == "":
            print("Invalid Input. Please enter 'yes' or 'no'.")
            continue  
        elif isStudent == "no":
            print("Thank you for using the system.")
            break  
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")
            continue  

