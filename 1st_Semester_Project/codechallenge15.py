import os

tuloy = True
no = 1  

while tuloy:
    ask = input("Do you wish to create a new triangle (yes or no)? ").strip().lower()

    if ask.lower == "no":
        print("Program/loop terminated")
        break
    elif ask.lower == "yes":
        os.system("cls") 

        no += 1

        for x in range(1, 6):
            for y in range(1, no + 1):  
                for z in range(1, x + 1):  
                    print("A", end="")
                print()  

            print()  

    else:
        os.system("cls")  
        print("Invalid answer, please only answer 'yes' or 'no'")
	
	continue
