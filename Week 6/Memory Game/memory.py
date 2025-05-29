import random

NUM_PAIRS = 3


def get_valid_index(displayed_list):
    """
    Get a valid index from the user.
    A valid index must be:
    - A number
    - Within bounds (0 to len(displayed_list) - 1)
    - Point to an unrevealed position (displayed_list[index] == '*')
    """
    while True:
        try:
            index = int(input("Enter an index: "))

            # Check if index is out of bounds
            if index < 0 or index >= len(displayed_list):
                print("Invalid index. Try again.")
                continue

            # Check if position is already revealed
            if displayed_list[index] != "*":
                print("This number has already been matched. Try again.")
                continue

            return index

        except ValueError:
            print("Not a number. Try again.")


def main():
    """
    Main function to run the memory game.
    """
    # Milestone #1: Create the truth list
    truth_list = []
    for i in range(NUM_PAIRS):
        truth_list.append(i)
        truth_list.append(i)

    # Milestone #2: Shuffle the list
    random.shuffle(truth_list)

    # Milestone #3: Create a displayed list
    displayed_list = ["*"] * len(truth_list)

    # Milestone #6: Play multiple turns until game is won
    while "*" in displayed_list:
        # Print the current display array
        print(displayed_list)

        # Milestone #4: Get two valid indices from the user
        first_index = get_valid_index(displayed_list)

        # Get second index, ensuring it's different from first
        while True:
            second_index = get_valid_index(displayed_list)

            # Check if user entered the same index twice
            if first_index == second_index:
                print("You entered the same index twice. Try again.")
            else:
                break

        # Milestone #5: Check if there's a match
        if truth_list[first_index] == truth_list[second_index]:
            # Match found - update displayed list
            displayed_list[first_index] = truth_list[first_index]
            displayed_list[second_index] = truth_list[second_index]
            print("Match!")
            clear_terminal()
        else:
            # No match - show values and wait
            print(
                "Value at index "
                + str(first_index)
                + " is "
                + str(truth_list[first_index])
            )
            print(
                "Value at index "
                + str(second_index)
                + " is "
                + str(truth_list[second_index])
            )
            print("No match. Try again.")
            input("Press Enter to continue... ")
            clear_terminal()

    # Game won - print final display and congratulations
    print(displayed_list)
    print("Congratulations! You won!")


def clear_terminal():
    for i in range(20):
        print("\n")


if __name__ == "__main__":
    main()
