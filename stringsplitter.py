#Name: Saba Ambreen
#Lesson 6.1: String Splitter

string = input("")

middle = string[len(string)//2]
first = string[0:len(string)//2]
second = string[len(string)//2+1:]

# printing result
print("middle character: " + middle)
print("first half: " + first)
print("second half: " + second)
