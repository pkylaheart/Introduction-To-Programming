a = 5    
for x in range(1, a + 1):
    for y in range(a, x, -1):
        print(" ", end = " ") 
    for v in range(x, 0, -1):
        print(v, end = " ")  
    for v in range(2, x + 1):
        print(v, end = " ")  
    print()  

for x in range(a - 1, 0, -1):
    for y in range(a, x, -1):
        print(" ", end = " ") 
    for v in range(x, 0, -1):
        print(v, end = " ")  
    for v in range(2, x + 1):
        print(v, end = " ") 
    print() 