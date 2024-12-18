import os
import time

def clear_screen():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def print_menu():
    while True:
        print("Let's get started with python printing. Pick any topic of printing in python below. \n ╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮\n\t     ⋘ PRINT STATEMENT ⋙ \n\n\t 1. PRINTING DATA TYPES \n\t 2. PRINTING WITH ESCAPE CHARACTER \n\t 3. COMMENTS \n\t 4. QUIT \n ╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯")
        print_ask = input("Enter number:  ")  

        clear_screen()

        if print_ask == '1':
            print_datatypes()
        elif print_ask == '2':
            escape_char()
        elif print_ask == '3':
            comments()
        elif print_ask == '4':
            menu() 
            break
        else:
            print("Invalid Input.. Try again \n")
            
def print_datatypes():
    print("\t     -- PRINTING DATA TYPES --")                 
    print("You can print any data type.")
    print("Pick any data type from below. Below are just a few data types of Python.")
    print("1. String \t 2. Float \n3. Boolean \t 4. Integer  \n\n  Press Any To Go Back.")
    ask_datatypes = input("\nEnter Number:  ")
    
    clear_screen()
    
    if ask_datatypes == '1':
        string()
    elif ask_datatypes == '2':
        float_()
    elif ask_datatypes == '3':
        boolean()
    elif ask_datatypes == '4':
        integer()
    else: 
        print("invalid input")
        clear_screen()
        print_datatypes

def string():
    while True:
        print("\t\t-- STRING --\n")
        print("Explanation: A string is a piece of text, like words or sentences. It's anything inside quotes.")
        print("Example Code:") 
        print("print('Hello World')\n")
        print("Output:")
        print("Hello World!\n\n")
        print("Try printing a String!")
        string = input("Input a word or letter: ")
        print(string)
        example = input("Do you want more example: (yes/no)")
        clear_screen()
        
        if example != 'yes':
            print("Thank you for exploring strings!")
            break
        
        clear_screen()
        from activity2 import example_on_input
        example_on_input()
        
            
        back1 = input("--------------------- \nPress Any to go back.")

        clear_screen()

        if input == input:
            print_datatypes()
            break
        else: 
            print("invalid input")
            continue

def boolean():
    while True:
            print("\t\t-- BOOLEAN --")
            print("A boolean is a type that can only have one of two values: True (yes) or False (no).\n")
            print("Example Code:") 
            print("is_raining = True")
            print("if is_raining:")
            print("\tprint('Take an umbrella!')\n") 
            print("Output:")
            print("Take an umbrella!\n")
            back1 = input("--------------------- \nPress 'Enter' to go back.")

            clear_screen()

            if input == input:
                print_datatypes()
                break
            else: 
                print("invalid input")
                continue

def integer():
    print("\t\t-- INTEGER --")
    print("An integer is a whole number without any decimal or fractional part.")
    print("Example Code:") 
    print("print(5)\n")
    print("Output:")
    print("5\n")    
    print("Try it!")

    while True:
        user_input = input("\nPlease enter a Number: ")
        try:
            number = int(user_input)
            print(f"You entered the integer: {number}")
            ask = input("--------------------- \nPress any key to go back: ")
                
            clear_screen()  
                
            if ask == ask:
                print_datatypes()
                break
        except ValueError:
            print("That is not a valid number.")
        
           

def float_():
    print("\t\t-- FLOAT --")
    print("\nA float is a number that can have a decimal point.")
    print("Example Code:") 
    print("print(2.0)\n")
    print("Output:")
    print("2.0\n")   
    print("Try it!")   

    while True:
        user_input = input("Please enter a float: ")
        if '.' not in user_input:
            print("That is not a valid float (needs to have a decimal point). Please enter a valid float.")
            continue
        else:
            print(f"You entered the float: {user_input}")
            ask = input("--------------------- \nPress any key to go back: ")
            
            clear_screen()  
            
            if ask == ask:
                print_datatypes()
                break
    

def escape_char():
    print("\t     -- PRINTING WITH ESCAPE CHARACTERS --")                 
    print("Below are just a few Escape Characters of Python.\n")
    print("1. New Line \t 2. Backslash \n3. Tab \t\t 4. Backspace \n\n  Press Any To Go Back.")
    ask_escapechar = input("\nEnter Number:  ")
    
    clear_screen()
    
    if ask_escapechar == '1':
        newline()
    elif ask_escapechar == '2':
        backslash()
    elif ask_escapechar == '3':
        tab()
    elif ask_escapechar == '4':
        backspace()
    else: 
        print("invalid input")
        clear_screen()
        escape_char

def newline():
    while True:
        print("\t\t-- NEW LINE --")
        print("' \\n ' Inserts a newline.\n")
        print("Code:") 
        print("print('Hello\\nWorld')\n")
        print("Output:")
        print("Hello\nWorld\n")
        ex = input("\nDo you want to try for yourself? (yes/no) : ") 

        clear_screen()

        if ex.lower() == 'yes':
            print("\t\t-- NEWLINE --")
            bs = input("Type a word: ")
            b2 = input("Type another word: ")
            print("\nOutput: ")
            print(f"\n{bs}\n\n{b2}")
            back1 = input("--------------------- \nPress Any to go back.")
            break
            clear_screen()
            escape_char()
            
        
        else: 
            clear_screen()
            escape_char()
            break

def tab():
    while True:
        print("\t\t-- TAB --")
        print("' \\t ' Used to insert a tab.\n")
        print("Code:") 
        print("print('Hello\\tWorld')\n")
        print("Output:")
        print("Hello\tWorld\n")
        ex = input("\nDo you want to try for yourself? (yes/no) : ") 
    
        clear_screen()

        if ex.lower() == 'yes':
            print("\t\t-- TAB --")
            bs = input("Type a word: ")
            b2 = input("Type another word: ")
            print("\nOutput: ")
            print(bs,"\t\t\t\t\t\t",b2)
            back1 = input("--------------------- \nPress Any to go back.")
            break
            clear_screen()
            escape_char()
            
        
        else: 
            clear_screen()
            escape_char()
            break

def backslash():
    while True:
        print("\t\t-- BACKSLASH --")
        print("' \\\\ ' This will insert one \\ (backslash).\n")
        print("Code:") 
        print("print('Hello\\\\World')\n")
        print("Output:")
        print("Hello\\World\n")
        ex = input("\nDo you want to try for yourself? (yes/no) : ") 
        
        clear_screen()

        if ex.lower() == 'yes':
            print("\t\t-- BACKSLASH --")
            bs = input("Type a word: ")
            b2 = input("Type another word: ")
            print("\nOutput: ")
            print(bs,"\\")
            print(b2,"\\n")
            back1 = input("--------------------- \nPress Any to go back.")
            break
            clear_screen()
            escape_char()
            
        
        else: 
            clear_screen()
            escape_char()
            break
def backspace():
    while True:
        print("\t\t-- BACKSPACE --")
        print("' \\b ' erases the previous character printed. \n")
        print("Code:") 
        print("print('Hello\\b World')\n")
        print("Output:")
        print("Hello\bWorld\n")
        ex = input("\nDo you want to try for yourself? (yes/no) :")
        
        clear_screen()

        if ex.lower() == 'yes':
            print("\t\t-- BACKSPACE --")
            bs = input("Type a word: ")
            bs = bs[:-1]
            print("\nOutput: ")
            print(bs)

            back1 = input("--------------------- \nPress Any to go back.")
            break
            clear_screen()
            escape_char()
            
        
        else: 
            clear_screen()
            escape_char()
            break
def comments():
    print("\t     -- COMMENTS --")                 
    print("#: Used for single-line comments.")
    print("Code:") 
    print("#Hello World\n")
    print("Output:\n")
    print("\n''' or \""": Used for multi-line comments")
    print("Code:") 
    print("'''Hello World'''\n")
    print("Output:\n")
    '''HelloWorld'''
    back1 = input("--------------------- \nPress Any to go back.")
    
    clear_screen()

def val_number(valid):
    while True:
        try:
            return int(input(valid))  # Try to convert the input to an integer
        except ValueError:
            print("Invalid input. Please enter a valid number.")  # Handle the error

def arithmetic_operations():
    print("\t\t-- ARITHMETIC OPERATIONS --")
    print("Choose an operation:")
    print("1. Addition (+) \t\t2. Subtraction (-)\t\t5. Modulus (%)")
    print("3. Multiplication (*) \t\t4. Division (/)\t\t\t6. Exponentiation (**) \t\t7. Back\n")
    
    choice = input("Pick an Operator: ")
    clear_screen()

    while True:
        if choice == ' ' or '':
            arithmetic_operations()
        elif choice == '7':
            clear_screen()
            menu()
        elif choice == '1':
            number1 = val_number("Enter the first number: ")
            number2 = val_number("Enter the second number: ")
            print(f"The sum of {number1} and {number2} is: {number1 + number2}")
            while True:    
                back1 = input("\nDo you want to perform another operation? (yes/no): ").lower()
                clear_screen()
                if back1 == 'yes':
                    clear_screen()
                    arithmetic_operations()
                    break
                elif back1 == 'no':
                    clear_screen()
                    menu()
                    break  
                else:
                    print("Invalid Choice, Try again")
                    continue
        elif choice == '2':
            number1 = val_number("Enter the first number: ")
            number2 = val_number("Enter the second number: ")
            print(f"The difference between {number1} and {number2} is: {number1 - number2}")
            while True:    
                back1 = input("\nDo you want to perform another operation? (yes/no): ").lower()
                clear_screen()
                if back1 == 'yes':
                    clear_screen()
                    arithmetic_operations()
                    break
                elif back1 == 'no':
                    clear_screen()
                    menu()
                    break  
                else:
                    print("Invalid Choice, Try again")
                    continue
        elif choice == '3':
            number1 = val_number("Enter the first number: ")
            number2 = val_number("Enter the second number: ")
            print(f"The product of {number1} and {number2} is: {number1 * number2}")
            while True:    
                back1 = input("\nDo you want to perform another operation? (yes/no): ").lower()
                clear_screen()
                if back1 == 'yes':
                    clear_screen()
                    arithmetic_operations()
                    break
                elif back1  == 'no':
                    clear_screen()
                    menu()
                    break  
                else:
                    print("Invalid Choice, Try again")
                    continue
        elif choice == '4':
            number1 = val_number("Enter the first number: ")
            number2 = val_number("Enter the second number: ")
            if number2 == 0:
                print("Error.")
                while True:    
                    back1 = input("\nDo you want to perform another operation? (yes/no): ").lower()
                    clear_screen()
                    if back1 == 'yes':
                        clear_screen()
                        arithmetic_operations()
                        break
                    elif back1  == 'no':
                        clear_screen()
                        menu()
                        break  
                    else:
                        print("Invalid Choice, Try again")
                        continue
            print(f"The quotient of {number1} divided by {number2} is: {number1 / number2}")
            while True:    
                back1 = input("\nDo you want to perform another operation? (yes/no): ").lower()
                clear_screen()
                if back1 == 'yes':
                    clear_screen()
                    arithmetic_operations()
                    break
                elif back1  == 'no':
                    clear_screen()
                    menu()
                    break  
                else:
                    print("Invalid Choice, Try again")
        elif choice == '5':
            number1 = val_number("Enter the first number: ")
            number2 = val_number("Enter the second number: ")
            if number2 == 0:
                print("Error.")
                while True:
                    back1 = input("\nDo you want to perform another operation? (yes/no): ").lower()
                    clear_screen()
                    if back1 == 'yes':
                        clear_screen()
                        arithmetic_operations()
                        break
                    elif back1  == 'no':
                        clear_screen()
                        menu()
                        break  
                    else:
                        print("Invalid Choice, Try again")
                        continue
            else:
                print(f"The modulus of {number1} and {number2} is: {number1 % number2}")
                while True:
                    back1 = input("\nDo you want to perform another operation? (yes/no): ").lower()
                    clear_screen()
                    if back1 == 'yes':
                        clear_screen()
                        arithmetic_operations()
                        break
                    elif back1 == 'no':
                        clear_screen()
                        menu()
                        break  
                    else:
                        print("Invalid Choice, Try again") 
                        continue
        
        elif choice == '6':
            number1 = val_number("Enter the first number: ")
            number2 = val_number("Enter the second number: ")
            print(f"The result of {number1} raised to the power of {number2} is: {number1 ** number2}")
            while True:    
                back1 = input("\nDo you want to perform another operation? (yes/no): ").lower()
                clear_screen()
                if back1 == 'yes':
                    clear_screen()
                    arithmetic_operations()
                    break
                elif back1  == 'no':
                    clear_screen()
                    menu()
                    break  
                else:
                    print("Invalid Choice, Try again")
                    continue
        else:
            print("Invalid choice. Please select a valid option.")
            while True:    
                back1 = input("\nDo you want to perform another operation? (yes/no): ").lower()
                clear_screen()
                if back1 == 'yes':
                    clear_screen()
                    arithmetic_operations()
                    break
                elif back1  == 'no':
                    clear_screen()
                    menu()
                    break  
                else:
                    print("Invalid Choice, Try again")
                    continue

def py_variables_menu():
    while True:
        print("Let's get started with Python Variables. Pick any topic of creating variables in python below. \n ╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮\n\t     ⋘ VARIABLES ⋙ \n\n\t 1. ASSIGN VARIABLES \n\t 2. OUTPUT VARIBLES \n\t 3. CASTING \n\t 4. QUIT \n ╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯")
        print_ask = input("Enter number:  ")  

        clear_screen()

        if print_ask == '1':
            create_var()
        elif print_ask == '2':
            multi_val()
        elif print_ask == '3':
            casting()
        elif print_ask == '4':
            menu() 
            break
        else:
            print("Invalid Input.. Try again \n")
            continue
def create_var():
    while True:
        print("\t\t-- CREATING VARIABLES --")
        print("Variables are for storing data called Values.")
        print("\nExample Code:") 
        print("x = 21\ny = 'Kyla'\n\nprint(x)\nprint(y)\n")
        print("Output:")
        print("5\nKyla")
        print("\nTry it!")
        while True:
            var = input("Enter variable name: ")
            if var == " " or var == '':
                print("No input found, try again")
                continue
            elif var[0].isdigit():
                print("Invalid variable name: Variable names cannot start with a number. Try again.")   
                continue 
            elif var.isidentifier():       
                val = input("Enter value: ")
                print(f"{var} = {val}")

                back1 = input("--------------------- \nPress Any to go back.")

                clear_screen()
                if input == input:
                    py_variables_menu()
                    break
                else: 
                    print("invalid input")
                    continue

def multi_val():
    while True:
        print("\t\t-- MULTIPLE VARIABLES --")
        print("You can assign multiple values in one time.")
        print("\nCode:") 
        print("a = 21, \nb = 'Kyla' \nc = 'Lucena City'\n\nprint(a ,b , c)\n")
        print("Output:")
        print("21 , Kyla, Lucena City\n")
        ex = input("\nDo you want to try for yourself? (yes/no)")
        if ex.lower() == 'yes':
            from activity3 import biodata
            clear_screen()
            biodata()
            
        else:
            clear_screen()
            py_variables_menu()
            break
        back1 = input("--------------------- \nPress Any to go back.")

        clear_screen()

        if input == input:
            py_variables_menu()
            break
        else: 
            print("invalid input")
            continue
def casting():
    while True:
        print("\t\t-- CASTING --")
        print("Specifying data types can be done with casting.")
        print("\nCode:") 
        print("a = str(7)\nb = int(7)\nc = float(7)\n\nprint(type(a))\nprint(type(b))\nprint(type(c))\n")
        print("Output:")
        print("<class 'str'>\n<class 'int>\n<class 'float'>\n")
        back1 = input("--------------------- \nPress Any to go back.")

        clear_screen()

        if input == input:
           py_variables_menu()
           break
        else: 
            print("invalid input")
            continue            
def py_conditional_menu():
    while True:
        print("Let's get started with Python Conditional Statements.")
        print("╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮")
        print("\t⋘ CONDITIONAL STATEMENTS ⋙")
        print("\t  1. IF STATEMENT")
        print("\t  2. ELIF STATEMENT")
        print("\t  3. ELSE STATEMENT")
        print("\t  4. LOGICAL OPERATORS")
        print("\t  5. COMPARING OPERATORS")
        print("\t  6. QUIT")
        print("╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯")
        print_ask = input("Enter number: ")

        clear_screen()

        if print_ask == '1':
            if_statement()
        elif print_ask == '2':
            elif_statement()
        elif print_ask == '3':
            else_statement()
        elif print_ask == '4':
            logical_operators_menu()
        elif print_ask == '5':
            comparing_operators()
        elif print_ask == '6':
            menu()
            break
        else:
            print("Invalid Input.. Try again\n")

def comparing_operators():
    while True:
        print("\t\t-- COMPARING OPERATORS --\n")
        print("1. == (EQUAL)\t\t\t\t\t 2. != (NOT EQUAL)")
        print("3. > (GREATER THAN)\t\t\t\t 4. < (LESS THAN)")
        print("5. >= (GREATER THAN OR EQUAL)\t\t\t 6. <= (LESS THAN OR EQUAL)\n")
        
        operator = input(" Select an Operator (1-6) \n(Press 'Enter' to go back.): ")
        clear_screen()

        if operator == '1':
            is_equal()
        elif operator == '2':
            is_notequal()
        elif operator == '3':
            greater()
        elif operator == '4':
            less()
        elif operator == '5':
            less_eq()
        elif operator == '6':
            greater_eq()
        else: 
            print("invalid input")
            clear_screen()
            py_conditional_menu()
    
    input("\nPress Enter to go back.")
    clear_screen()
    py_conditional_menu()

def is_equal():
    print("Checks if two values are exactly the same.\n")
    print("Code: 5 == 5 \nOutput:", 5 == 5)
    input("\nPress Enter to go back.")
    clear_screen()
    comparing_operators()
def is_notequal():
    print("Checks if two values are not the same.\n")
    print("Code: 5 != 3 \nOutput:", 5 != 3)
    input("\nPress Enter to go back.")
    clear_screen()
    comparing_operators()
def greater():
    print("Checks if the left value is larger than the right value.\n")
    print("Code: 5 > 3 \nOutput:", 5 > 3)
    input("\nPress Enter to go back.")
    clear_screen()
    comparing_operators()
def less():
    print("Checks if the left value is smaller than the right value.\n")
    print("Code: 5 < 3 \nOutput:", 5 < 3)
    input("\nPress Enter to go back.")
    clear_screen()
    comparing_operators()
def greater_eq():
    print("Checks if the left value is larger than or equal to the right value.\n")
    print("Code: 5 >= 3 \nOutput:", 5 >= 3)
    input("\nPress Enter to go back.")
    clear_screen()
    comparing_operators()
def less_eq():
    print("Checks if the left value is smaller than or equal to the right value.\n")
    print("Code: 5 <= 3 \nOutput:", 5 <= 3)
    input("\nPress Enter to go back.")
    clear_screen()
    comparing_operators()

def if_statement():
    print("\t\t-- IF STATEMENT --")
    print("Explanation: The 'if' statement allows you to execute a block of code only if a specified condition is True.")
    print("Code:")
    print("x = 5\nif x > 3:\n\tprint('x is greater than 3')")
    print("Output:")
    x = 5
    if x > 3:
        print("x is greater than 3\n")
    while True:
            ask1 = input("Do you want to try it? [yes/no] ")
            if ask1.lower() == 'yes':
                clear_screen()
                print("Loading... ")
                time.sleep(2)
                clear_screen()
                print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                print("     Greater Than or less Than ")
                print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                num = input("Enter a number: ")

                try:
                    num = int(num)
                    
                    if num < 10:
                        print(f"The number {num} is less than 10.")
                        input("\nPress 'Enter' to go back.")
                        clear_screen()
                        break
                    if num == 10:
                        print("The number is exactly 10.")
                        input("\nPress 'Enter' to go back.")
                        clear_screen()
                        break
                    if num > 10:
                        print(f"The number {num} is greater than 10.")
                        input("\nPress 'Enter' to go back.")
                        clear_screen()
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif ask1.lower() == 'no':
                clear_screen()
                py_conditional_menu()
            elif ask1.lower() == " " or '':
                continue

def elif_statement():
    print("\t\t-- ELIF STATEMENT --")
    print("Explanation: The 'elif' (short for 'else if') statement is used to check multiple conditions.")
    print("Code:")
    print("x = 5\nif x > 10:\n\tprint('x is greater than 10')\nelif x > 3:\n\tprint('x is greater than 3')")
    print("Output:")
    x = 5
    if x > 10:
        print("x is greater than 10\n")
    elif x > 3:
        print("x is greater than 3\n")
        while True:
            ask1 = input("Do you want to try it? [yes/no] ")
            if ask1.lower() == 'yes':
                clear_screen()
                print("Loading... Activity10")
                time.sleep(2)
                clear_screen()
                print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                print("     DLL IDENTIFICATION ")
                print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                from activity10 import identification
                identification()
                while True:
                    ask2 = input("\nDo you want to try another example? [yes/no] ")
                    if ask2.lower() == 'yes':
                        clear_screen()
                        print("Loading... Code Challenge 4")
                        time.sleep(2)
                        clear_screen()
                        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                        print("           GROCERY   ")
                        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                        from codechallenge4 import grocery
                        grocery()
                        input("\nPress 'Enter' to go back.")
                        clear_screen()
                        py_conditional_menu()
                    elif ask2.lower() == 'no':
                        clear_screen()
                        py_conditional_menu()
                    elif ask2.lower() == " " or '':
                        continue
            elif ask1.lower() == 'no':
                clear_screen()
                py_conditional_menu()
            elif ask1.lower() == " " or '':
                continue
    


def else_statement():
    print("\t\t-- ELSE STATEMENT --")
    print("Explanation: The 'else' statement is used when all previous conditions in 'if' and 'elif' have failed.")
    print("Code:")
    print("x = 2\nif x > 3:\n\tprint('x is greater than 3')\nelse:\n\tprint('x is not greater than 3')")
    print("Output:")
    x = 2
    if x > 3:
        print("x is greater than 3\n")
    else:
        print("x is not greater than 3\n")
    while True:
            ask1 = input("Do you want to try it? [yes/no] ")
            if ask1.lower() == 'yes':
                clear_screen()
                print("Loading... Activity 7")
                time.sleep(2)
                clear_screen()
                print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                print("     GOLD IDENTIFIER ")
                print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                from activity7 import gold_identifier
                gold_identifier()
                ask2 = input("\nDo you want to try another example? [yes/no] ")
                if ask2.lower() == 'yes':
                    clear_screen()
                    print("Loading... Activity 8")
                    time.sleep(2)
                    clear_screen()
                    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                    print("          PASSWORD ")
                    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                    from activity8 import password
                    password()
                    input("\nPress 'Enter' to go back.")
                    clear_screen()
                    break
                elif ask2.lower() == 'no':
                    clear_screen()
                    py_conditional_menu()
                elif ask2.lower() == " " or '':
                    continue
            elif ask1.lower() == 'no':
                clear_screen()
                py_conditional_menu()
            elif ask1.lower() == " " or '':
                continue

def logical_operators_menu():
    while True:
        print("\t\t-- LOGICAL OPERATORS -- \n")
        
        print("1. AND \t\t\t4. OR \n2. NOT \t\t\t5. IS \n3. IS NOT \t\t6. BACK")
        operator_choice = input("\nEnter number:  ")
        clear_screen()

        if operator_choice == '1':
            and_operator()
        elif operator_choice == '4':
            or_operator()
        elif operator_choice == '2':
            not_operator()
        elif operator_choice == '5':
            is_operator()
        elif operator_choice == '3':
            is_not_operator()
        elif operator_choice == '6':
            py_conditional_menu() 
            break
        else:
            print("Invalid Input.. Try again \n")

def and_operator():
    print("The `and` operator returns `True` if both conditions are true.\n")
    print("Example:")
    print("x = 7")
    print("y = 8")
    print("if x > 5 and y < 10: print('Both conditions are true')")
    print("\nOutput:")
    
    x = 7
    y = 8
    if x > 5 and y < 10:
        print("Both conditions are true\n")
    else:
        print("One or both conditions are false")
    while True:
        ask1 = input("Do you want to try it for youself? [yes/no] ")
        if ask1.lower() == 'yes':
            clear_screen()
            print("Loading... Activity9")
            time.sleep(2)
            clear_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("\t AND Operator ")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            from activity9 import age_cal
            age_cal()
            input("\nPress 'Enter' to go back.")
            clear_screen()
            break
        elif ask1.lower() == 'no':
            clear_screen()
            logical_operators_menu()
        elif ask1.lower() == " " or '':
            continue
        

def or_operator():
    print("The `or` operator returns `True` if at least one condition is true.\n")
    print("Example:")
    print("x = 4")
    print("y = 8")
    print("if x > 5 or y < 10: print('At least one condition is true')")
    print("\nOutput:")
    
    x = 4
    y = 8
    if x > 5 or y < 10:
        print("At least one condition is true")
    else:
        print("Both conditions are false\n")
    while True:
        ask1 = input("Do you want to try it for youself? [yes/no] ")
        if ask1.lower() == 'yes':
            clear_screen()
            print("Loading...")
            time.sleep(2)
            clear_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("\t  OR Operator ")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))
            
            if num1 > 10 or num2 > 10:
                print("At least one of the numbers is greater than 10.")
            else:
                print("Neither of the numbers is greater than 10.")
                input("\nPress 'Enter' to go back.")
                clear_screen()
                break
        elif ask1.lower() == 'no':
            clear_screen()
            logical_operators_menu()
        elif ask1.lower() == " " or '':
            continue

def not_operator():
    print("The `not` operator returns `True` if the condition is false.\n")
    print("Example:")
    print("x = 4")
    print("if not(x > 5): print('Condition is false')")
    print("\nOutput:")
    
    x = 4
    if not(x > 5):
        print("Condition is false")
    else:
        print("Condition is true\n")
    
    while True:
        ask1 = input("Do you want to try it for youself? [yes/no] ")
        if ask1.lower() == 'yes':
            clear_screen()
            print("Loading...")
            time.sleep(2)
            clear_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("\t  NOT Operator ")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

            has_ticket_input = input("Do you have a ticket? (yes/no): ").lower()
            if has_ticket_input == "yes":
                has_ticket = True
            else:
                has_ticket = False

            if not has_ticket:
                print("You need a ticket to enter.")
                break
            else:
                print("You can enter with your ticket. Enjoy the event!")
                input("\nPress 'Enter' to go back.")
                clear_screen()
                break
        elif ask1.lower() == 'no':
            clear_screen()
            logical_operators_menu()
        elif ask1.lower() == " " or '':
            continue

def is_operator():
    print("The `is` operator checks if two variables refer to the same object.\n")
    print("Example:")
    print("x = [1, 2, 3]")
    print("y = x")
    print("if x is y: print('x and y are the same object')")
    print("\nOutput:")
    
    x = [1, 2, 3]
    y = x  
    if x is y:
        print("x and y are the same object\n")
    else:
        print("x and y are different objects\n")
    
    while True:
        ask1 = input("Do you want to try it for youself? [yes/no] ")
        if ask1.lower() == 'yes':
            clear_screen()
            print("Loading...")
            time.sleep(2)
            clear_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("\t  IS Operator ")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            user_input = input("Enter something (or leave blank): ")
            if user_input is None:
                print("You didn't enter anything (input is None).")
            else:
                print(f"You entered: {user_input}")
                input("\nPress 'Enter' to go back.")
                clear_screen()
                break
        elif ask1.lower() == 'no':
            clear_screen()
            logical_operators_menu()
        elif ask1.lower() == " " or '':
            continue

def is_not_operator():
    print("The `is not` operator checks if two variables refer to different objects.\n")
    print("Example:")
    print("x = [1, 2, 3]")
    print("y = [1, 2, 3]")
    print("if x is not y\n\tprint('x and y are different objects')\nelse:\n\tprint('x and y are the same object)")
    print("\nOutput:")
    
    x = [1, 2, 3]
    y = [1, 2, 3]  
    if x is not y:
        print("x and y are different objects\n")
    else:
        print("x and y are the same object\n")
    while True:
        ask1 = input("Do you want to try it for youself? [yes/no] ")
        if ask1.lower() == 'yes':
            clear_screen()
            print("Loading...")
            time.sleep(2)
            clear_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("\tIS NOT Operator ")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            def check_value(value):
                while True:
                    if value is not None:
                        print(f"The value is {value}.")
                        input("\nPress 'Enter' to go back.")
                        clear_screen()
                        logical_operators_menu()

                    else:
                        print("The value is None.")
                        input("\nPress 'Enter' to go back.")
                        clear_screen()
                        logical_operators_menu()
            user_input = input("Enter something: ")
            check_value(user_input)  
            check_value(None)
          
                
        elif ask1.lower() == 'no':
            clear_screen()
            logical_operators_menu()
        elif ask1.lower() == " " or '':
            continue


def py_loop_menu():
    while True:
        print("Let's get started with Python Looping. Pick any topic of loops below.")
        print("╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮")
        print("\t     ⋘ LOOPS ⋙")
        print("\t 1. FOR LOOP")
        print("\t 2. WHILE LOOP")
        print("\t 3. QUIT")
        print("╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯")
        print_ask = input("Enter number: ")

        clear_screen()

        if print_ask == '1':
            for_loop()
        elif print_ask == '2':
            while_loop()
        elif print_ask == '3':
            menu()
            break
        else:
            print("Invalid Input.. Try again\n")


def for_loop():
    print("\t\t-- FOR LOOP --")
    print("Explanation: A 'for' loop is used to iterate over a sequence (like a list or a range).")
    print("It automatically handles the loop counter and stops when the sequence ends.")
    print("Code:")
    print("for i in range(5):\n\tprint(i)")
    print("Output:")
    for i in range(5):
        print(i)
    print()    
    while True:
        ask1 = input("Do you want to try it? [yes/no] ")
        if ask1.lower() == 'yes':
            clear_screen()
            print("Loading... Activity 11")
            time.sleep(2)
            clear_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("          FOR LOOP  ")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            from activity11 import loopingname_ex1
            loopingname_ex1()
            while True:
                ask2 = input("\nDo you want to try another example? [yes/no] ")
                if ask2.lower() == 'yes':
                    clear_screen()
                    print("Loading... Activity 12")
                    time.sleep(2)
                    clear_screen()
                    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                    print("          ODD OR EVEN ")
                    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                    from activity12 import forloop_ex2
                    forloop_ex2()
                    while True:
                        ask3 = input("\nDo you want to try another example? [yes/no] ")
                        if ask3.lower() == 'yes':
                            clear_screen()
                            print("Loading... Activity 13")
                            time.sleep(2)
                            clear_screen()
                            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                            print("          FACTORIAL ")
                            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                            from activity13 import forloop_ex3
                            forloop_ex3()
                            while True:
                                ask4 = input("\nDo you want to try another example? [yes/no] ")
                                if ask4.lower() == 'yes':
                                    clear_screen()
                                    print("Loading... Activity 14")
                                    time.sleep(2)
                                    clear_screen()
                                    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                                    print("          FOR LOOP [2] ")
                                    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                                    from activity14 import forloop_ex4
                                    forloop_ex4()
                                    while True:
                                        ask5 = input("\nDo you want to try another example? [yes/no] ")
                                        if ask5.lower() == 'yes':
                                            clear_screen()
                                            print("Loading... Activity 15")
                                            time.sleep(2)
                                            clear_screen()
                                            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                                            print("          FOR LOOP [3] ")
                                            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                                            from activity15 import forloop_ex5
                                            forloop_ex5()
                                            while True:
                                                ask6 = input("\nDo you want to try another example? [yes/no] ")
                                                if ask6.lower() == 'yes':
                                                    clear_screen()
                                                    print("Loading... Activity 16")
                                                    time.sleep(2)
                                                    clear_screen()
                                                    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                                                    print("          FOR LOOP [4] ")
                                                    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                                                    from activity16 import forloop_ex6
                                                    forloop_ex6()
                                                    while True:
                                                        ask7 = input("\nDo you want to try another example? [yes/no] ")
                                                        if ask7.lower() == 'yes':
                                                            clear_screen()
                                                            print("Loading... Activity 17")
                                                            time.sleep(2)
                                                            clear_screen()
                                                            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                                                            print("          FOR LOOP [5] ")
                                                            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                                                            from activity17 import forloop_ex7
                                                            forloop_ex7()
                                                            while True:
                                                                ask8 = input("\nDo you want to try another example? [yes/no] ")
                                                                if ask8.lower() == 'yes':
                                                                    clear_screen()
                                                                    print("Loading... Activity 18")
                                                                    time.sleep(2)
                                                                    clear_screen()
                                                                    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                                                                    print("          FOR LOOP [6] ")
                                                                    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                                                                    from activity18 import forloop_ex8
                                                                    forloop_ex8()
                                                                    while True:
                                                                        ask9 = input("\nDo you want to try another example? [yes/no] ")
                                                                        if ask9.lower() == 'yes':
                                                                            clear_screen()
                                                                            print("Loading... Activity 19")
                                                                            time.sleep(2)
                                                                            clear_screen()
                                                                            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                                                                            print("          FOR LOOP [7] ")
                                                                            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                                                                            from activity19 import forloop_ex9
                                                                            forloop_ex9()
                                                                            input("\nPress 'Enter' to go back.")
                                                                            clear_screen()
                                                                            py_loop_menu()
                                                                        elif ask9.lower() == 'no':
                                                                            clear_screen()
                                                                            py_loop_menu()
                                                                        elif ask9.lower() == " " or '':
                                                                            continue
                                                                elif ask8.lower() == 'no':
                                                                    clear_screen()
                                                                    py_loop_menu()
                                                                elif ask8.lower() == " " or '':
                                                                    continue
                                                        elif ask7.lower() == 'no':
                                                            clear_screen()
                                                            py_loop_menu()
                                                        elif ask7.lower() == " " or '':
                                                            continue
                                                elif ask6.lower() == 'no':
                                                    clear_screen()
                                                    py_loop_menu()
                                                elif ask6.lower() == " " or '':
                                                    continue
                                        elif ask5.lower() == 'no':
                                            clear_screen()
                                            py_loop_menu()
                                        elif ask5.lower() == " " or '':
                                            continue
                                elif ask4.lower() == 'no':
                                    clear_screen()
                                    py_loop_menu()
                                elif ask4.lower() == " " or '':
                                    continue
                        elif ask3.lower() == 'no':
                            clear_screen()
                            py_loop_menu()
                        elif ask3.lower() == " " or '':
                            continue
                elif ask2.lower() == 'no':
                    clear_screen()
                    py_loop_menu()
                elif ask2.lower() == " " or '':
                    continue
        elif ask1.lower() == 'no':
            clear_screen()
            py_loop_menu()
        elif ask1.lower() == " " or '':
            continue
        
    
def while_loop():
    print("\t\t-- WHILE LOOP --")
    print("Explanation: A 'while' loop repeatedly executes a block of code as long as the given condition is True.")
    print("It requires explicit management of the loop counter or condition inside the loop.")
    print("Code:")
    print("i = 0\nwhile i < 5:\n\tprint(i)\n\ti += 1")
    print("Output:")
    i = 0
    while i < 5:
        print(i)
        i += 1
    print()
    while True:
        ask8 = input("\nDo you want to try another example? [yes/no] ")
        if ask8.lower() == 'yes':
            clear_screen()
            print("Loading... Activity 20")
            time.sleep(2)
            clear_screen()
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print("          TRIANGLE ")
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            from activity20 import whileloop_ex1
            whileloop_ex1()
            while True:
                ask9 = input("\nDo you want to try another example? [yes/no] ")
                if ask9.lower() == 'yes':
                    clear_screen()
                    print("Loading... Activity 21")
                    time.sleep(2)
                    clear_screen()
                    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                    print("             NAME ")
                    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                    from activity21 import whileloop_ex2
                    whileloop_ex2()
                    input("\nPress 'Enter' to go back.")
                    clear_screen()
                    py_loop_menu()
                elif ask9.lower() == 'no':
                    clear_screen()
                    py_loop_menu()
                elif ask9.lower() == " " or '':
                    continue
        elif ask8.lower() == 'no':
            clear_screen()
            py_loop_menu()
        elif ask8.lower() == " " or '':
            continue
    


def py_functions_menu():
    while True:
        print("Let's get started with Python Functions. Pick any topic of functions below.")
        print("╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮")
        print("\t     ⋘ FUNCTIONS ⋙")
        print("\t 1. FUNCTION SYNTAX")
        print("\t 2. FUNCTION RETURN")
        print("\t 3. FUNCTION ARGUMENTS")
        print("\t 4. QUIT")
        print("╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯")
        print_ask = input("Enter number: ")

        clear_screen()

        if print_ask == '1':
            func_syntax()
        elif print_ask == '2':
            func_return()
        elif print_ask == '3':
            func_args()
        elif print_ask == '4':
            menu()
            break
        else:
            print("Invalid Input.. Try again\n")

def func_syntax():
    while True:
        print("\t\t-- FUNCTION SYNTAX --")
        print("Explanation: A function is defined using the 'def' keyword. Functions allow you to group code into reusable blocks.")
        print("Code:") 
        print("def my_function():\n\tprint('Hello World')\nmyfunctions()\n")
        print("Output:")
        print("Hello World\n")
        back1 = input("--------------------- \nPress Any to go back.")

        clear_screen()

        if input == input:
            py_functions_menu()
            break

def func_return():
    while True:
        print("\t\t-- FUNCTION RETURN --")
        print("Explanation: Functions can return values using the 'return' keyword, which can then be used elsewhere in the program.")
        print("Code:") 
        print("def my_function():\n\treturn 5\nprint(my_function())\n")
        print("Output:")
        print("5\n")
        back1 = input("--------------------- \nPress Any to go back.")

        clear_screen()

        if input == input:
            py_functions_menu()
            break
        

def func_args():
    while True:
        print("\t\t-- FUNCTION ARGUMENTS --")
        print("Explanation: Functions can accept arguments, which are values passed to the function when it is called.")
        print("Code:") 
        print("def greet(name):\n\tprint('Hello ' + name)\n\ngreet('Alice')\n")
        print("Output:")
        print("Hello Alice")
        back1 = input("--------------------- \nPress Any to go back.")

        clear_screen()

        if input == input:
            py_functions_menu()
            break

def py_list_menu():
    while True:
        print("Let's get started with Python Lists.")
        print("╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮")
        print("\t     ⋘ LISTS ⋙")
        print("\t 1. LIST CREATION")
        print("\t 2. ACCESSING LIST ELEMENTS")
        print("\t 3. ADDING ELEMENTS")
        print("\t 4. REMOVE ITEM FROM LIST")
        print("\t 5. QUIT")
        print("╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯")
        print_ask = input("Enter number: ")

        clear_screen()

        if print_ask == '1':
            list_creation()
            break
        elif print_ask == '2':
            accessing_list_elements()
            break
        elif print_ask == '3':
            adding_elements()
            break
        elif print_ask == '4':
            remove_from_list()
            break
        elif print_ask == '5':
            menu()
            break
        else:
            print("Invalid Input.. Try again\n")

def remove_from_list():
        my_list = [1, 2, 3, 4, 5]
        print("\t\t-- REMOVE ITEM FROM LIST --\n")
        print("Explanation: The 'remove()' method removes the first occurrence of a specified element from a list.")
        print(f"Original List: {my_list}")
        print("my_list.remove(1)\n")
        print("Output:")
        my_list.remove(1)
        print(my_list)
        input("\nPress 'Enter' to go back.")
        clear_screen()
        py_list_menu()


def list_creation():
    print("\t\t-- LIST CREATION --")
    print("Explanation: Lists in Python are ordered collections of items, defined using square brackets [].")
    print("Code:")
    print("my_list = [1, 2, 3, 'hello']\n")
    print("Output:")
    my_list = [1, 2, 3, 'hello']
    print(my_list)
    input("\nPress Enter to go back.")
    clear_screen()
    py_list_menu()


def accessing_list_elements():
    print("\t\t-- ACCESSING LIST ELEMENTS --")
    print("Explanation: You can access elements of a list using their index, starting from 0.")
    print("Code:")
    print("my_list = [1, 2, 3, 'hello']\nprint(my_list[0]\n") 
    print("Output:")
    my_list = [1, 2, 3, 'hello']
    print(my_list[0])
    input("\nPress Enter to go back.")
    clear_screen()
    py_list_menu()


def adding_elements():
    print("\t\t-- ADDING ELEMENTS TO A LIST --")
    print("Explanation: The 'append()' method adds an element to the end of the list.")
    print("Code:")
    print("my_list = [1, 2, 3]\nmy_list.append(4)\nprint(my_list)\n")
    print("Output:")
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)
    input("\nPress Enter to go back.")
    clear_screen()
    py_list_menu()

def menu():
    while True:
        print("╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮\n\t     ⋘ MAIN MENU ⋙ \n\n\t 1. PRINT STATEMENT \n\t 2. VARIABLES  \n\t 3. ARITHMETIC OPERATORS \n\t 4. CONDITIONAL STATEMENTS  \n\t 5. LOOP STATEMENTS \n\t 6. FUNCTIONS \n\t 7. LIST \n\t 8. QUIT \n\n ╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯")
        option = input("Enter a number:  ")
        
        clear_screen()

        if option == '1':
            print_menu()
            break
        elif option == '2':
            py_variables_menu()
            break
        elif option == '3':
            arithmetic_operations()
            break
        elif option == '4':
            py_conditional_menu()
            break
        elif option == '5':
            py_loop_menu()
            break
        elif option == '6':
            py_functions_menu()
            break
        elif option == '7':
            py_list_menu()
            break
        elif option == '8':
            print("Program Terminated..")
            break
        else:
            print("Invalid option, Try again!")
            continue
menu()
# while True:
#     name = input("Good day! May I know your name? ").title()
#     print(f"Hi, {name}")
#     start = input("Do you want to start the Program? (Yes/No) \n --> ")
    
#     clear_screen()

#     if start.lower() == "yes":
#         print("Lets Start!")
#         menu()
#         break
#     else:
#         print("Okay, Have a great day!")
#         break