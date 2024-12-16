
import os

def clear_screen():
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

def print_menu():
    while True:
        print("Let's get started with python printing. Pick any topic of printing in python below. \n ╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮\n\t     ⋘ PRINT STATEMENT ⋙ \n\n\t 1. PRINTING DATA TYPES \n\t 2. PRINTING WITH ESCAPE CHARACTER \n\t 3. COMMENTS \n\t 4. QUIT \n ╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯")
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
            print("\t\t-- STRING --")
            print("Code:") 
            print("print('Hello World')\n")
            print("Output:")
            print("Hello World!\n")
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
            print("Code:") 
            print("print(True)\n")
            print("Output:")
            print("True\n")
            back1 = input("--------------------- \nPress Any to go back.")

            clear_screen()

            if input == input:
                print_datatypes()
                break
            else: 
                print("invalid input")
                continue

def integer():
    while True:
            print("\t\t-- INTEGER --")
            print("Code:") 
            print("print(5)\n")
            print("Output:")
            print("5\n")
            back1 = input("--------------------- \nPress Any to go back.")

            clear_screen()

            if input == input:
                print_datatypes()
                break
            else: 
                print("invalid input")
                continue

def float_():
    while True:
            print("\t\t-- FLOAT --")
            print("Code:") 
            print("print(2.0)\n")
            print("Output:")
            print("2.0\n")
            back1 = input("--------------------- \nPress Any to go back.")

            clear_screen()

            if input == input:
                print_datatypes()
                break
            else: 
                print("invalid input")
                continue

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
            back1 = input("--------------------- \nPress Any to go back.")

            clear_screen()

            if input == input:
                escape_char()
                break
            else: 
                print("invalid input")
                continue
def tab():
    while True:
            print("\t\t-- TAB --")
            print("' \\t ' Used to insert a tab.\n")
            print("Code:") 
            print("print('Hello\\tWorld')\n")
            print("Output:")
            print("Hello\tWorld\n")
            back1 = input("--------------------- \nPress Any to go back.")

            clear_screen()

            if input == input:
                escape_char()
                break
            else: 
                print("invalid input")
                continue
def backslash():
    while True:
        print("\t\t-- BACKSLASH --")
        print("' \\\\ ' This will insert one \\ (backslash).\n")
        print("Code:") 
        print("print('Hello\\\\World')\n")
        print("Output:")
        print("Hello\\World\n")

        back1 = input("--------------------- \nPress Any to go back.")

        clear_screen()

        if input == input:
            escape_char()
            break
        else: 
            print("invalid input")
            continue
def backspace():
    while True:
        print("\t\t-- BACKSPACE --")
        print("' \\b ' erases the previous character printed. \n")
        print("Code:") 
        print("print('Hello\\b World')\n")
        print("Output:")
        print("Hello\bWorld\n")
        back1 = input("--------------------- \nPress Any to go back.")

        clear_screen()

        if input == input:
            escape_char()
            break
        else: 
            print("invalid input")
            continue

def comments():
    print("\t     -- COMMENTS --")                 
    print("#: Used for single-line comments.")
    print("Code:") 
    print("#Hello World\n")
    print("Output:\n")
    #HelloWorld # the ouput didn't show but it should appear like this #HelloWorld
    print("\n''' or \""": Used for multi-line comments")
    print("Code:") 
    print("'''Hello World'''\n")
    print("Output:\n")
    '''HelloWorld'''
    back1 = input("--------------------- \nPress Any to go back.")
    
    clear_screen()
    
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
def create_var():
     while True:
        print("\t\t-- CREATING VARIABLES --")
        print("Variables are for storing data called Values.")
        print("\nCode:") 
        print("x = 21\ny = 'Kyla'\n\nprint(x)\nprint(y)\n")
        print("Output:")
        print("5\nKyla")
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
        print("\t     ⋘ CONDITIONAL STATEMENTS ⋙")
        print("\t 1. IF STATEMENT")
        print("\t 2. ELIF STATEMENT")
        print("\t 3. ELSE STATEMENT")
        print("\t 4. LOGICAL OPERATORS")
        print("\t 5. QUIT")
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
            menu()
            break
        else:
            print("Invalid Input.. Try again\n")


def if_statement():
    print("\t\t-- IF STATEMENT --")
    print("Code:")
    print("x = 5\nif x > 3:\n\tprint('x is greater than 3')")
    print("Output:")
    x = 5
    if x > 3:
        print("x is greater than 3")
    input("\nPress Enter to go back.")
    clear_screen()
    py_conditional_menu()


def elif_statement():
    print("\t\t-- ELIF STATEMENT --")
    print("Code:")
    print("x = 5\nif x > 10:\n\tprint('x is greater than 10')\nelif x > 3:\n\tprint('x is greater than 3')")
    print("Output:")
    x = 5
    if x > 10:
        print("x is greater than 10")
    elif x > 3:
        print("x is greater than 3")
    input("\nPress Enter to go back.")
    clear_screen()
    py_conditional_menu()


def else_statement():
    print("\t\t-- ELSE STATEMENT --")
    print("Code:")
    print("x = 2\nif x > 3:\n\tprint('x is greater than 3')\nelse:\n\tprint('x is not greater than 3')")
    print("Output:")
    x = 2
    if x > 3:
        print("x is greater than 3")
    else:
        print("x is not greater than 3")
    input("\nPress Enter to go back.")
    clear_screen()
    py_conditional_menu()

def logical_operators_menu():
    while True:
        print("Logical Operators Menu: \n")
        print("1. and \n2. or \n3. not \n4. is \n5. is not \n6. Back")
        operator_choice = input("\nEnter number:  ")

        clear_screen()

        if operator_choice == '1':
            and_operator()
        elif operator_choice == '2':
            or_operator()
        elif operator_choice == '3':
            not_operator()
        elif operator_choice == '4':
            is_operator()
        elif operator_choice == '5':
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
        print("Both conditions are true")
    else:
        print("One or both conditions are false")
    
    input("\nPress Any to go back.")
    clear_screen()

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
        print("Both conditions are false")
    
    input("\nPress Any to go back.")
    clear_screen()

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
        print("Condition is true")
    
    input("\nPress Any to go back.")
    clear_screen()

def is_operator():
    print("The `is` operator checks if two variables refer to the same object.\n")
    print("Example:")
    print("x = [1, 2, 3]")
    print("y = x")
    print("if x is y: print('x and y are the same object')")
    print("\nOutput:")
    
    x = [1, 2, 3]
    y = x  # y refers to the same object as x
    if x is y:
        print("x and y are the same object")
    else:
        print("x and y are different objects")
    
    input("\nPress Any to go back.")
    clear_screen()

def is_not_operator():
    print("The `is not` operator checks if two variables refer to different objects.\n")
    print("Example:")
    print("x = [1, 2, 3]")
    print("y = [1, 2, 3]")
    print("if x is not y: print('x and y are different objects')")
    print("\nOutput:")
    
    x = [1, 2, 3]
    y = [1, 2, 3]  # y refers to a different object than x, even though the contents are the same
    if x is not y:
        print("x and y are different objects")
    else:
        print("x and y are the same object")
    
    input("\nPress Any to go back.")
    clear_screen()


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
    while True:
        print("\t\t-- FOR LOOP --")
        print("Code:")
        print("for i in range(5):\n\tprint(i)")
        print("Output:")
        for i in range(5):
            print(i)
        input("\nPress Enter to go back.")
        clear_screen()
        if input == input:
            py_loop_menu()
            break
        else: 
            print("invalid input")
            continue          
        
    
def while_loop():
    while True:
        print("\t\t-- WHILE LOOP --")
        print("Code:")
        print("i = 0\nwhile i < 5:\n\tprint(i)\n\ti += 1")
        print("Output:")
        i = 0
        while i < 5:
            print(i)
            i += 1
        input("\nPress Enter to go back.")
        clear_screen()
        if input == input:
            py_loop_menu()
            break
        else: 
            print("invalid input")
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
        print("\t 4. QUIT")
        print("╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯")
        print_ask = input("Enter number: ")

        clear_screen()

        if print_ask == '1':
            list_creation()
        elif print_ask == '2':
            accessing_list_elements()
        elif print_ask == '3':
            adding_elements()
        elif print_ask == '4':
            menu()
            break
        else:
            print("Invalid Input.. Try again\n")


def list_creation():
    print("\t\t-- LIST CREATION --")
    print("Code:")
    print("my_list = [1, 2, 3, 'hello']")
    print("Output:")
    my_list = [1, 2, 3, 'hello']
    print(my_list)
    input("\nPress Enter to go back.")
    clear_screen()
    py_list_menu()


def accessing_list_elements():
    print("\t\t-- ACCESSING LIST ELEMENTS --")
    print("Code:")
    print("my_list = [1, 2, 3, 'hello']\nprint(my_list[0]") 
    print("Output:")
    my_list = [1, 2, 3, 'hello']
    print(my_list[0])
    input("\nPress Enter to go back.")
    clear_screen()
    py_list_menu()


def adding_elements():
    print("\t\t-- ADDING ELEMENTS TO A LIST --")
    print("Code:")
    print("my_list = [1, 2, 3]\nmy_list.append(4)\nprint(my_list)")
    print("Output:")
    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)
    input("\nPress Enter to go back.")
    clear_screen()
    py_list_menu()

def menu():
    while True:
        print("╭┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮\n\t     ⋘ MAIN MENU ⋙ \n\n\t 1. PRINT STATEMENT \n\t 2. VARIABLES  \n\t 3. CONDITIONAL STATEMENTS \n\t 4. LOOP STATEMENTS \n\t 5. FUNCTIONS \n\t 6. LIST \n\t 7. QUIT \n\n ╰┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╯")
        option = input("Enter a number:  ")
        
        clear_screen()

        if option == '1':
            print_menu()
            break
        elif option == '2':
            py_variables_menu()
            break
        elif option == '3':
            py_conditional_menu()
            break
        elif option == '4':
            py_loop_menu()
            break
        elif option == '5':
            py_functions_menu()
            break
        elif option == '6':
            py_list_menu()
            break
        elif option == '7':
            print("Program Terminated..")
            break
        else:
            print("Invalid option, Try again!")
            continue


while True:
    name = input("Good day! May I know your name? ").title()
    print(f"Hi, {name}")
    start = input("Do you want to start the Program? (Yes/No) \n --> ")
    
    clear_screen()

    if start.lower() == "yes":
        print("Lets Start!")
        menu()
        break
    else:
        print("Okay, Have a great day!")
        break