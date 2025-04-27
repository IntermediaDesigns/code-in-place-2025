from stanfordkarel import * #karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():
    while front_is_clear():
        if beepers_present():
            build_hospital() #Define function step
        else:
            move()

def build_hospital(): #Function to build a hospital
    turn_left()
    for i in range(2):
        move()
        put_beeper()
    turn_right() #Define function step
    move()
    put_beeper()
    turn_right()
    while front_is_clear():
        move()
        put_beeper()
    turn_left()
    if front_is_clear():
        move()

def turn_right(): #Defined step
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    run_karel_program()