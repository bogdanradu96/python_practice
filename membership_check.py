from datetime import datetime

def membership_check():
    current_date = datetime.now().date() #Get the system date as a date format from datetime
    creation_date = datetime.strptime(
        input("Enter the date when the membership was created (YYYY-MM-DD):"),
        "%Y-%m-%d"
    ).date() #Convert the user provided date from str to date format
    duration = int(input("Enter the duration of the membership in days:"))
    remaining_time = duration - (current_date - creation_date).days
    expired = True if (current_date - creation_date).days > duration else False #Operator ternar

    if expired is True:
        print("Your membership has expired")
    else:
        print(f"Your membership is still available and you have {remaining_time} days left.") #Output formatting with f-string