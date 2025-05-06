A cheat-sheet with the structure of the Karel programming language. See the Karel Reader for more details:

Base Karel commands

move()
turn_left()
put_beeper()
pick_beeper()

Karel program structures

This is the structure of a Karel program

from karel.stanfordkarel import *

# Comments can be included in any part
# of a program. They start with a #
# and include the rest of the line.
# the computer will ignore them, but they
# are very helpful for human readers!

def main():
    # code to execute

# declarations of other functions

# necessary boilerplate to start execution
if __name__ == '__main__':
    main()



# example program to move, put_beeper, move
def main():
    move()
    put_beeper()
    move()

# necessary boilerplate to start execution
if __name__ == '__main__':
    main()

Function Declaration:

def name():
    # body of the function.

# example: turn_right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


Conditions:

if condition:
    # code run if condition passes


if condition:
    # code block for "yes"
else:
    #code block for "no"


# example: a safe move
if front_is_clear():
    move()


For Loop:

for i in range(count):
    # code to repeat



# example: place 100 beepers
for i in range(100):
    put_beeper()



While Loop:

while condition:
    # code to repeat


# example: move karel to the next wall
while front_is_clear():
    move()


Names of the conditions

# karel conditions
front_is_clear()
beepers_present()
beepers_in_bag()
left_is_clear()
right_is_clear()
facing_north()
facing_south()
facing_east()
facing_west()



# opposites
front_is_blocked()
no_beepers_present()
no_beepers_in_bag()
left_is_blocked()
right_is_blocked()
not_facing_north()
not_facing_south()
not_facing_east()
not_facing_west()


Additional commands:

For advanced Karel programs you can use these three secret commands

random(p)
paint_corner(color)  # use "transparent" to remove colors
corner_color_is(color)



Here is a simple program that shows each of the advanced commands

def main():
    # this will pass 80% of the time
    if random(0.8):
        # create a blue square
        paint_corner("blue")
    # checks if the current square is blue
    if corner_color_is("blue"):
        move()