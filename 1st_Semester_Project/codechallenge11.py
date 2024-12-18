for x in range (1, 6):
    for y in range (7, x , -1):
        print("  ", end = " ")
    for v in range (3, x + 1):
        print(" *", end = " ")
    for v in range (4, x + 1):
        print(" *", end = " ")
    for y in range (6, x, -1):
        print("  ", end = " ")
    print()    
for x in range (1, 6):
    for y in range (1, x + 1):
        print("  ", end = " ")
    for v in range (5, x, -1):
        print(" *", end = " ")
    for v in range (4, x, -1):
        print(" *", end = " ")
    for y in range (1, x + 1):
        print("  ", end = " ")
    print()
    
