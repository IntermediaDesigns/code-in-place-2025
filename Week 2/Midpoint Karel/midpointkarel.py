from stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""


def main():
    go_to_side()
    move_karel()


# Function to have Karel pick up beeper to move closer to middle
def move_karel():
    while no_beepers_present():
        get_to_midpoint()

    pick_beeper()
    turn_back_around()
    turn_around()


# Function for Karel to go left and right
def go_to_side():
    # Make Karel go to the right, place a beeper
    while front_is_clear() and no_beepers_present():
        move()
    put_beeper()
    turn_back_around()

    # Make Karle go to the left, place a beeper
    while front_is_clear() and no_beepers_present():
        move()
    put_beeper()
    turn_back_around()


# Function to keep moving
def get_to_midpoint():
    while front_is_clear() and no_beepers_present():
        move()
    pick_beeper()
    turn_back_around()
    put_beeper()
    move()


# Function to turn Karel around
def turn_back_around():
    turn_left()
    turn_left()
    move()


# Function to turn karel around in a spot
def turn_around():
    turn_left()
    turn_left()
    if facing_west():
        turn_left()
        turn_left()


if __name__ == "__main__":
    main()
