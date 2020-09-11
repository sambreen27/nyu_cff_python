#Name: Saba Ambreen
#Lesson 4.1: BMI Metric With Status Category

kg = float(input())
height = float(input())

bmi = (kg/(height * height))

if bmi < 18.5:
    print("BMI is: {:.2f},".format(bmi),"Status is Underweight")
elif bmi <= 24.9:
    print("BMI is: {:.2f},".format(bmi),"Status is Normal")
elif bmi <= 29.9:
    print("BMI is: {:.2f},".format(bmi),"Status is Overweight")
else:
    print("BMI is: {:.2f},".format(bmi),"Status is Obese")
