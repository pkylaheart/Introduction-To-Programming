def age_cal():
	while True: 
		age = input("Enter your age: ")

		try:
			age = int(age)
			
			if age >= 1 and age <= 7:
				print("That age is categorized as a Toddler.")
				break
			elif age >= 8 and age <= 13:
				print("That age is categorized as a Pre-Teen.")
				break
			elif age >= 14 and age <= 18:
				print("That age is categorized as a Teenager.")
				break
			elif age >= 19 and age <= 31:
				print("That age is categorized as Early Adulthood.")
				break
			elif age >= 32 and age <= 45:
				print("That age is categorized as Mid Adulthood.")
				break
			elif age >= 46 and age <= 59:
				print("That age is categorized as Post Adulthood.")
				break
			elif age >= 60 and age <= 100:
				print("That age is categorized as Senior.")
				break
			else:
				print("Invalid Age")

		except ValueError:
			print("Please enter a valid number for age.")