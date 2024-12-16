#Identify and count if it's gold

gold = 0
miner = input("Hi, What is your name: ").title()
isGold = input("Is the mineral Gold? ")

if isGold.lower() == 'yes':
    gold += 1
    print(f"Hi {miner}, The total number of gold is {gold}.")
else: 
    print(f"Hi {miner}, The total number of gold is {gold}.")
