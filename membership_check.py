from datetime import datetime
#o mica verificare poate cu comprehension sau ternar
#un print cu f

def membership_check():
    current_date = datetime.now().date()
    creation_date = datetime.strptime(input("Enter the date when the membership was created (YYYY-MM-DD):"), "%Y-%m-%d").date()
    duration = int(input("Enter the duration of the membership in days"))
    print("Diferenta", current_date - creation_date)
    print("Your membership has expired" if (current_date - creation_date).days > duration else "Membership available") #Operator ternar