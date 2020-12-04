#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This program is an updated guessing game

import random


def main():
    # this function compares an integer to a random number

    print("Today we will play a guessing game.")

    # random number generation
    random_number = random.randint(0, 9)

    # input
    user_guess = input("Enter a number between 0-9: ")
    print("")

    # process
    try:
        user_guess_int = int(user_guess)

        if user_guess_int == random_number:
            # output
            print("Correct! {} was the right answer."
                  .format(random_number))
        else:
            # output
            print("Incorrect, {} was the right answer."
                  .format(random_number))
    except Exception:
        # output
        print("That's not a number! Try again.")
    finally:
        # output
        print("")
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
