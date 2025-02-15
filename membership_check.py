from datetime import datetime

def membership_check(creation_date_str: str, duration: int, current_date: str = None):

    if current_date is None: #Checks if a date was provided if not uses the system date, used for testing.
        current_date = datetime.now().date() #Get the system date as a date format from datetime
    else:
        current_date = datetime.strptime(current_date, "%Y-%m-%d").date()

    creation_date = datetime.strptime(creation_date_str, "%Y-%m-%d").date() #Convert the user provided date from str to date format
    remaining_time = duration - (current_date - creation_date).days
    expired = True if (current_date - creation_date).days >= duration else False #Operator ternar

    if expired is True:
        return "Your membership has expired"
    else:
        return f"Your membership is still available and you have {remaining_time} days left." #Output formatting with f-string
