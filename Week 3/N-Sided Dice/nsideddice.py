import random


def main():
    """Write a program which takes as input the number of sides on a dice.  Then, simulate rolling a dice with that many sides. Print the outcome of the roll. When you're done, click on the "Check Correct" button.

    Here is the terminal output for an example run of the program (user input in blue):

    How many sides does your dice have? 10
    Your roll is 8"""

    # Get the number of sides from the user
    sides = int(input("How many sides does your dice have? "))

    # Simulate rolling the dice
    roll = random.randint(1, sides)

    # Print the outcome of the roll
    print(f"Your roll is {roll}")


if __name__ == "__main__":
    main()
