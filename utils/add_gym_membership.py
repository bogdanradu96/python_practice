import csv
import os
from pathlib import Path


class Membership:
    """
    Initializes a Membership object.

    Parameters:
    -----------
    name : str
    duration : int (days)
    price : float ($)
    benefits : list (optional)
    """
    def __init__(self, name, duration, price, benefits = None):
        self.name = name
        self.duration = duration
        self.price = price
        self.benefits = benefits if benefits else ["No benefits included"]

    def to_dict(self):
        return {
            "name": self.name,
            "duration": self.duration,
            "price": self.price,
            "benefits": self.benefits
        }
    def __str__(self):
        return str(self.to_dict())

def add_gym_membership():
    """
    Requests details to add a new membership package
    """
    name = input("Enter the name of the membership:")
    duration = int(input("Enter the duration of the membership in days:"))
    price = float(input("Enter the price in $:"))

    benefits_option = input("Enter the benefits - 1 for no benefits, 2 for One or more benefits:")
    benefits = []

    if benefits_option == "2":
        while True:
            benefit = input(" Enter a benefit(press enter to stop):")
            if benefit == "":
                break
            benefits.append(benefit)

    membership = Membership(name, duration, price, benefits)
    print("Membership addded!", membership)

    #Checking if the user wants to add another offer
    more = input("Would you like to add another membership?")
    if more.lower() == 'yes':
        add_gym_membership()

    #Saving the membership packages in a csv file
    #file_path = 'C:/Users/bogda/Desktop/PythonSkillab/citygym/memberships.csv'

    project_root = Path(__file__).resolve().parent.parent #Gets the root directory two levels up from "scripts"

    #Defines the output directory and file path
    folder_path = project_root / 'data'
    file_path = folder_path / 'memberships.csv'

    with open(file_path, "a", newline="") as csvfile:
        file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0 # Checking if the file exists and is not empty
        fieldnames = ["name", "duration", "price", "benefits"] #A list of what the field names should be
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames) #Defining the writer for easier use

        if file_exists is False: #Writes the dictionary keys as headers if the file does not exist
            writer.writeheader()

        writer.writerows([membership.to_dict()]) #Writing the dictionary content in rows
    print("Membership(s) saved in memberships.csv")