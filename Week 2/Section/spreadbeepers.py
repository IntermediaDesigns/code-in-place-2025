from stanfordkarel import *

"""
Each row starts in front of a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""

# The main function to run your defined functions to move Karel and place 4 beepers int he row.
def main():
    move()
    spread_beepers()
    step_back()

# Define a variable to combine all of your defined parts
def spread_beepers():
    while beepers_present():
        pick_beeper()
        if beepers_present():
            move_to_end()
            put_beeper()
            reset()
    put_beeper()

# Define a variable to have Karel keep moving if beepers present
def move_to_end():
    while beepers_present():
        move()

# Define a variable to combine other functions for Karel
def reset():
    turn_around()
    move_to_wall()
    turn_around()
    move()

# Define a variable to have Karel keep moving while the front is clear
def move_to_wall():
    while front_is_clear():
        move()

# Define a variable to have Karel turn around
def turn_around():
    turn_left()
    turn_left()

# Define a variable to have Karel go back to the beginning
def step_back():
    turn_around()
    move()
    turn_around()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    main()
