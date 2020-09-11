#Name: Saba Ambreen
#Lesson 4.2: Cash Register

firstItem = float(input())
secondItem = float(input())
cc = input("")
taxRate = float(input())
taxRate = taxRate/100

basePrice = float(firstItem + secondItem)
print("base price = {:.2f}".format(basePrice))

if(firstItem <= secondItem):
    firstItem = firstItem * .50
else:
    secondItem = secondItem * .50

basePrice = firstItem + secondItem

if (cc == 'y'):
    discountPrice = (basePrice - (basePrice * .10))
else:
    discountPrice = basePrice

print("price after discounts = {:.2f}".format(discountPrice))

totalPrice = discountPrice + (discountPrice * taxRate)

print("total price = {:2.2f}".format(totalPrice))
