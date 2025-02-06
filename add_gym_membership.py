def add_gym_membership():
    '''
    Add new membership package

    Examples:
    ----------
    add_gym_membership()
    '''

    name = input("Enter the name of the membership:")
    valability = input("Enter the duration of the membership:")
    price = input("Enter the price:")
    benefits = input("Enter the benefits - 1 for no benefits, 2 for multiple ones:")

    if int(benefits) == 1:

        benefits = "No benefits included"
        membership = {
            'name' :name,
            'valability' :valability,
            'price' :price,
            'benefits' :benefits
        }
        print("Membership added!", membership)

    else:
        pass
