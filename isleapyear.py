#Name: Saba Ambreen
#Lesson 7.1: Leap Year Function
year = 2000

def isleapyear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False

isleapyear(year)
