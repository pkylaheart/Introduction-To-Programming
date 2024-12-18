def gold_identifier():

    miner = input("Hi, What is your name: ").title()
    
    isGold = input("Is the mineral Gold? (yes/no): ").lower()

    while isGold not in ['yes', 'no']:  
        print("Invalid input. Please respond with 'yes' or 'no'.")
        isGold = input("Is the mineral Gold? (yes/no): ").lower()

    # If the mineral is gold
    if isGold == "yes":
        while True:
            try:
                count = int(input("How many pieces of gold do you have? "))
                if count < 0:
                    print("Please enter a positive whole number.")
                    continue  
                print(f"Hi {miner}, The total number of gold is {count}.")
                break  
            except ValueError:
                print("Invalid input. Please enter a valid whole number.")
    else:
        print(f"Hi {miner}, The total number of gold is 0.")
        

