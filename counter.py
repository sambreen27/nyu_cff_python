#Name: Saba Ambreen
#Lesson 3: 1 - Coin Counter

print("# of quarters: ")
quarters = int(input())
print("# of dimes: ")
dimes = int(input())
print("# of nickels: ")
nickels = int(input())
print("# of pennies: ")
pennies = int(input())

total = (quarters * 25 + dimes * 10 + nickels * 5 + pennies)
dollars = int(total/100)
cents = int(total%100)
print ("The total is",  dollars ,"dollars and", cents, "cents")
