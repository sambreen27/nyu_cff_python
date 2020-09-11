#Name: Saba Ambreen
#Lesson 8.2: Max Absolute In List Function

input_values = [-19, -3, 20, -1, 0, -25]

def max_abs_val(input_values):
    absolute_values = [abs(x) for x in input_values]
    return max(absolute_values)

max_abs_val(input_values)
