# birthday countdown lab
#import datetime module
import datetime 
# ask the name of user
name = input("Please Enter Your Name.")
print ("Hello " + name)
birthdate = input("Please Enter Your Birthday in MM/DD/YYYY. ")
print  ("Your Birthday is " + birthdate)
birthdate = datetime.datetime.strptime(birthdate,'%m/%d/%Y').date()
# calculate the number of days till birthdate
today = datetime.date.today()
if (today.month, today.day) > (birthdate.month, birthdate.day):
    # birthdate has already passed 
    birthday = datetime.date(today.year+1, birthdate.month, birthdate.day)
else:
    # birtdate has not passed yet 
    birthday = datetime.date(today.year, birthdate.month, birthdate.day)
days_until_birthday = (birthday - today).days
# print the number of days till birthdate
print(f"hello,{name} Your Birthday is in {days_until_birthday} days.")

# check if the user birtdate is today and print happy birthday
if today.month == birthdate.month and today.day == birthdate.day: 
    print ("Happy Birthday!")
