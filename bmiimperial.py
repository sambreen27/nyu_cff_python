#Name: Saba Ambreen
#Lesson 3.4: BMI Imperial

pounds = 0.453592
inches = 0.0254
kg = float(input())*pounds
height = float(input())*inches

BMI = (kg/(height * height))

print("bmi is: {:.10f}".format(BMI))
