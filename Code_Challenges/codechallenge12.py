for x in range (1,5):
	for y in range (5, x, -1):
		print(" ", end = " ")
	for u in range (1, x + 1):
		print("*", end = " ")
	for u in range (1, x + 1):
		print("*", end = " ")
	print()
for x in range (1,5):
	for y in range (5, x, -1):
		print(" ", end = " ")
	for y in range (2, x + 1):
		print(" ", end = " ")
	for y in range (1,3):
		print("*", end = " ")
	print()