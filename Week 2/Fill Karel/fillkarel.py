from stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    # Fill the world row by row
    while front_is_clear():
        fill_row()
        move_to_next_row()


def fill_row():
    # Place beeper at current position if needed
    if no_beepers_present():
        put_beeper()

    # Fill rest of the row
    while front_is_clear():
        move()
        if no_beepers_present():
            put_beeper()


def move_to_next_row():
    while front_is_blocked():
        turn_left()
    while front_is_clear():
        move()
    turn_right()
    if front_is_clear():
        move()
        turn_right()
    else:
        turn_right()
        while front_is_clear():
            move()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    main()
