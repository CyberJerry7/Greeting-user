import time

print("\n\n")

timeNow = time.strftime('%I:%M %p')
time12hrs = int(time.strftime('%I'))
time24hrs = int(time.strftime('%H'))
date = time.strftime('%d/%m/%Y')
day = time.strftime('%A')
am_pm = time.strftime('%p')

userName = input("Hey User, Enter your name: ")

print("\n\n****************************\n\n")

print("Date: ",date)
print("Day: ", day)
print("Time: ", timeNow)
print("\n")

name = userName.capitalize()

if (time24hrs>=5 and time24hrs<12):
    print("\t\t\tGood Morning,", name , end="!")

elif(time24hrs>=12 and time24hrs<18):
    print("\t\t\tGood Afternoon,", name, end="!")

elif(time24hrs>=18 and time24hrs<21):
    print("\t\t\tGood Evening,", name, end="!")    

elif(time24hrs>=21 and time12hrs<5 and am_pm=="AM"):
    print("\t\t\tGood Night,", name, end="!")

print("\n\n\n")