#Name: Saba Ambreen
#Lesson 3.2: Coin Converter

print("Please enter the amount of money to convert:")
dollars = int(input("# of dollars: "))
cents = int(input("# of cents: "))

total = (int(dollars*100+cents))

quarters = int(total/25)
total = (total%25)

dimes = int(total/10)
total = (total%10)

nickels = int(total/5)
total = (total%5)

pennies = int(total/1)
total = (total%1)

print("The coins are", quarters, "quarters,", dimes, "dimes,", nickels, "nickels and", pennies, "pennies")
