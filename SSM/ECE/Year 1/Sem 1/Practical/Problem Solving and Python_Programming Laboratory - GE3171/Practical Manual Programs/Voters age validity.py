import datetime

Year_of_birth = int(input("In which year you look birth : "))
current_year = datetime.datetime.now().year
Current_age = current_year - Year_of_birth
print("Your current age is ", Current_age)

if (Current_age <= 18):
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")
