from stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    fill_column()
    fill_row()
    next_row()


# Fill column with a beeper in every other
def fill_column():
    turn_left()
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    turn_around()
    move_to_wall()
    turn_left()


# Fill rows with beepers
def fill_row():
    if beepers_present():
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()
    else:
        while front_is_clear():
            move()
            put_beeper()
            if front_is_clear():
                move()
    turn_around()
    move_to_wall()
    turn_around()


# Go to next row to fill beepers
def next_row():
    while left_is_clear():
        turn_left()
        move()
        face_east()
        fill_row()
    face_east()
    move_to_wall()
    turn_left()


# Turn Karel around
def turn_around():
    turn_left()
    turn_left()


# Move Karel to wall
def move_to_wall():
    while front_is_clear():
        move()


# Face Karel to East
def face_east():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    main()
