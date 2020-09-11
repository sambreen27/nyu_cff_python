#Name: Saba Ambreen
#Lesson 4.2: Cash Register

weekdays = ["Mon", "Tue", "Wed", "Thr", "Fri"]
weekend = ["Sat","Sun"]

day = input("")
time = int(input(""))
call_time = int(input(""))

if (day in weekdays):
    if(time >= 800 and time <= 1800):
        call_rate = call_time * 0.40
        total_cost = print("This call will cost ${:.2f}".format(call_rate))

    elif(time >= 1801 and time <= 2400):
        call_rate = call_time * 0.25
        total_cost = print("This call will cost ${:.2f}".format(call_rate))

    elif(time >= 0000 and time <= 759):
        call_rate = call_time * 0.25
        total_cost = print("This call will cost ${:.2f}".format(call_rate))

if(day in weekend and time <= 2400):
    call_rate = call_time * 0.15
    total_cost = print("This call will cost ${:.2f}".format(call_rate))
