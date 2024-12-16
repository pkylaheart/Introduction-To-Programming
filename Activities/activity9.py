age = eval(input(" Enter your age: "))

if age >= 1 and age <= 7 :
	print("That age  is categorized as a Toddler.")

elif age >= 8 and age <= 13 :
	print("That age  is categorized as a Pre-Teen.")

elif age >= 14 and age <= 18 :
	print("That age  is categorized as a Teenager.")

elif age >= 19 and age <= 31 :
	print("That age  is categorized as a Early Adulthood.")

elif age >= 32 and age <= 45 :
	print("That age  is categorized as a Mid Adulthood.")

elif age >= 46 and age <= 59 :
	print("That age  is categorized as a Post Adulthood.")

elif age >= 60 and age <= 100 :
	print("That age  is categorized as a Senior.")

else:
	print("Invalid Age")