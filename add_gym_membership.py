def add_gym_membership():
    '''
    Add new membership package

    Examples:
    ----------
    add_gym_membership()
    '''

    name = input("Enter the name of the membership:")
    duration = int(input("Enter the duration of the membership in days:"))
    price = float(input("Enter the price in $:"))
    benefits = input("Enter the benefits - 1 for no benefits, 2 for One or more benefits:")
    membership_package = {}
    if int(benefits) == 1:

        benefits = "No benefits included"
        membership = {
            'name' :name,
            'duration' :duration,
            'price' :price,
            'benefits' :benefits
        }
        print("Membership added!", membership)
        membership_package.update(membership)

    else:
        benefits = []
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
        membership_package.update(membership)
    print("Available memberships", membership_package)