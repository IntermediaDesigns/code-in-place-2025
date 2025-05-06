from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""


def main():
    # Build all columns
    for i in range(4):
        build_column()
        move_to_next_column()


def build_column():
    # Turn to face north (up)
    turn_left()

    # Place 5 beepers to build the column
    for i in range(5):
        put_beeper()
        if front_is_clear():
            move()

    # Return to the bottom of the column
    turn_around()

    # Move back down (skip the bottom beeper we already placed)
    for i in range(4):
        move()

    # Turn to face east (right) again
    turn_left()


def move_to_next_column():
    # Move to the next column (4 spaces)
    for i in range(4):
        if front_is_clear():
            move()


def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    main()
