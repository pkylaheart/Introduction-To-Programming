def grocery(): 
    while True:
        buygrocery = input("Did you buy a grocery? [Yes or No] ").lower() 

        if buygrocery == 'yes':
            item_name = input("Name of the item: ")

            while True:
                try:
                    item_price = float(input("Price of the item: "))
                    amount = float(input("Amount given: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter numeric values for price and amount.")

            tax_rate = 0.123 
            total = item_price * (1 + tax_rate)
        
            discount_rate = 0.052
            discount = round(discount_rate * total, 2)
            senior = total - discount

            while True:
                try:
                    age = int(input("Input your age: "))
                    if age <= 0 or age >= 150:
                        print("Invalid age entered. Please enter a valid age.")
                        continue
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid integer for age.")

            if age >= 60:  
                print(f"Hi, customer! You purchased a {item_name} with a price of {item_price} plus 12.3% tax.")
                print(f"Total amount to pay with tax: {total}")
                print(f"Amount given: {amount}")
                print(f"Senior discount: {discount}")
                print(f"Your change is: {round(amount - senior, 2)}.")
            else:  
                change = amount - total 
                print(f"Hi, customer! You purchased a {item_name} with a price of {item_price} plus 12.3% tax.")
                print(f"Total amount to pay with tax: {total}")
                print(f"Amount given: {amount}")
                print(f"Your change is: {round(change, 2)}")

            break

        elif buygrocery == 'no':
            print("Thank you for dropping by!")
            break  

        else:
            print("Invalid input! Please enter 'Yes' or 'No'.")  
            continue  
