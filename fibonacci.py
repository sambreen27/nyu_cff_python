#Name: Saba Ambreen
#Lesson 5.2: Fibonacci

n = int(input(""))

v1 = 0
v2 = 1

for num in range(1, n+1):
           if(num <= 1):
                next = num
           else:
                next = v1 + v2
                v1 = v2
                v2 = next
           print(next)
