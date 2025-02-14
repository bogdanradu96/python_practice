import os
import sys

sys.path.append((os.path.dirname(os.getcwd()))) # Append path to travelagency

import add_gym_membership as gym
import membership_check as check
import view_memberships as view


if __name__ == "__main__":

        task = input("What would you like to do? 1 - add new membership, 2 - check availability, 3 - view memberships:\n")
        if task == "1":
            gym.add_gym_membership()
        elif task == "2":
            check.membership_check()
        elif task == "3":
            view.view_memberships()
        else:
            print("That option is not available")