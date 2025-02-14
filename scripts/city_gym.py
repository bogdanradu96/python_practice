import os
import sys

sys.path.append((os.path.dirname(os.getcwd()))) # Append path to travelagency

import add_gym_membership as gym
import membership_check as check


if __name__ == "__main__":

        task = input("What would you like to do? 1 - add new membership, 2 - check availability:\n")
        if task == "1":
            gym.add_gym_membership()
        elif task == "2":
            check.membership_check()
        else:
            print("That option is not available")