import os
import sys

sys.path.append((os.path.dirname(os.getcwd()))) # Append path to citygym

import add_gym_membership as gym
import membership_check as check
import view_memberships as view


if __name__ == "__main__":

    #Create an exception for tasks
    class TaskException(Exception):
        pass

try:
    task = input("What would you like to do? 1 - add new membership, 2 - check availability, 3 - view memberships:\n")
    if task == "1":
        gym.add_gym_membership()
    elif task == "2":
        creation_date = input("Enter the date when the membership was created (YYYY-MM-DD):")
        duration = int(input("Enter the duration of the membership in days:"))
        print(check.membership_check(creation_date, duration))
    elif task == "3":
        view.view_memberships()
    else:
        raise TaskException #We raise the self-made exception if the input is incorrect
except TaskException:
    print("Option not available")