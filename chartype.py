#Name: Saba Ambreen
#Lesson 6.2: Character Type

count = 0
while (count < 4):
    count = count + 1
    x = input("")
    if (x.isdigit()):
        print(x, "is a digit.")
    elif (x.islower()):
        print(x, "is a lower case letter.")
    elif (x.isupper()):
        print(x, "is an upper case letter.")
    else:
        print(x, "is a non-alphanumeric character.")
