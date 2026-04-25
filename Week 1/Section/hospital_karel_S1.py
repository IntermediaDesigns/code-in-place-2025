from karel.stanfordkarel import *

# So while Karel checks if the front is clear to safely move 
# and if there is a beeper present, Karel will build hospital
def main():
    while front_is_clear():
        if beepers_present():
            build_hospital()
        safe_move()

# Define a variable for Karel to turn around
def turn_around():
    turn_left()
    turn_left()

# Define a variable to place 3 beepers
def place_three_beepers():
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

# Define a variable for Karel to go to bottom of column 
# from the top
def move_to_bottom():
    while front_is_clear():
        move()

# Define a variable for Karel to return back to the bottom 
# of the column
def return_to_bottom():
    turn_around()
    move_to_bottom()

# Define a variable to build 1 column
def make_one_column():
    turn_left()
    place_three_beepers()
    return_to_bottom()
    turn_left()

# Define a variable to combine the columns to build hospital
def build_hospital():
    pick_beeper()
    make_one_column()
    move()
    make_one_column()

# Define a variable for Karel to check if it is safe to move
def safe_move():
    if front_is_clear():
        move()


# don't change this code
if __name__ == '__main__':
    main()