for x in range (10, 0, -1):
	space = 10 - x
	for i in range (space):
		print("  ", end = "")
	for y in range (x):
		print(" *", end = "")
	print()