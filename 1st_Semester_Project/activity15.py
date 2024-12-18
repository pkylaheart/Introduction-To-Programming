def forloop_ex5():
    for x in range (0, 11):
        print(x, end = " ")
        for i in range (0, x):
            print("*", end = " ")
        print()