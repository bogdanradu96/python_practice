import csv


def add_gym_membership():
    """
    Requests details to add a new membership package

    Parameters:
    -----------
    name : str
    duration : int
    price : float
    benefits : str

    Examples:
    ----------
    add_gym_membership()
    """

    name = input("Enter the name of the membership:")
    duration = int(input("Enter the duration of the membership in days:"))
    price = float(input("Enter the price in $:"))
    benefits = input("Enter the benefits - 1 for no benefits, 2 for One or more benefits:")
    membership_packages = []
    #Checking if benefits need to be added in the offer\
    if int(benefits) == 1:

        benefits = "No benefits included"
        membership = {
            'name' :name,
            'duration' :duration,
            'price' :price,
            'benefits' :benefits
        }
        print("Membership added!", membership)
        membership_packages.append(membership)
    else:
        benefits = [] #Creates a list for benefits in case more are added
        while True:
            benefit = input("Enter the benefit:")
            if benefit == "":
                break

            benefits.append(benefit)
            print("Inserted benefits:", benefits)

        membership ={
            'name': name,
            'duration': duration,
            'price': price,
            'benefits': benefits
        }
        print("Membership added!", membership)
        membership_packages.append(membership)

    #Checking if the user wants to add another offer
    more = input("Would you like to add another membership?")
    if more == 'Yes':
        add_gym_membership()

    print("Available memberships:", membership_packages)
    with open('C:/Users/bogda/Desktop/PythonSkillab/citygym/memberships.csv', "a", newline="") as csvfile:
        fieldnames = membership_packages[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(membership_packages)