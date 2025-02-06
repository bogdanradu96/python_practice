import add_gym_membership as gym
import membership_check as check


if __name__ == "__main__":

    task = input("What would you like to do? 1 - add new membership, 2 - check availability:\n")
    if task == "1":
        gym.add_gym_membership()
    else:
        check.membership_check()