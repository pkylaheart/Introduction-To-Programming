buygrocery = input("Did you buy a grocery? [Yes or No] " )

if buygrocery.lower() == 'yes' :
	item_name = input("Name of the item: ")
	item_price = eval(input("Price of the item: "))
	amount = eval(input("Amount given: "))
	total = (item_price * 0.123) + item_price #the price of the item added taxation
	change = amount - total # applicable to those without discount
	discount = round((0.052 * total),2) #amount of discount for seniors
	senior = total - discount #substracting the discount to the total amount

	age = eval(input("Input your age: "))
	if age <= 0 or age >= 150 :
		print("Invalid Age")
	elif age >= 60 :
		print(f"Hi, customer you purchased a {item_name} , with a price of {item_price} plus 12.3% tax.")
		print(f"Total amount to pay with tax is {total}")
		print(f"Amount given is {amount}")
		print(f"Senior discount {discount}")
		print(f"Your change is {round((amount - senior),2)}.")
	else:
		print(f"Hi, customer you purchased a {item_name} , with a price of {item_price} plus 12.3% tax.")
		print(f"Total amount to pay with tax is {total}")
		print(f"Amount given is {amount}")
		print(f"Your change is {round(change, 2)}")
else:
	print("Thank you for dropping by!")