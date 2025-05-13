def main():
    """
    You should write your code here.
    """
    stones = 20

    current_player = 1

    while stones > 0:

        print(f"There are {stones} stones left.")

        stones_to_remove = int(
            input(f"Player {current_player} would you like to remove 1 or 2 stones? ")
        )

        while stones_to_remove != 1 and stones_to_remove != 2:
            stones_to_remove = int(input("Please enter 1 or 2: "))

        stones -= stones_to_remove

        if stones <= 0:
            winner = 2 if current_player == 1 else 1
            print()
            print(f"Player {winner} wins!")
            break
        current_player = 2 if current_player == 1 else 1

        print()


if __name__ == "__main__":
    main()
