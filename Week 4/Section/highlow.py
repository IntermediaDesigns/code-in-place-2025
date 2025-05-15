import random

NUM_ROUNDS = 5


def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # TODO: Write your code here!!! :)

    # Starting score
    score = 0

    # Print current round
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        # Generate the random numbers
        computer_number = random.randint(1, 100)
        user_number = random.randint(1, 100)

        # See your number
        print(f"Your number is {user_number}")

        # Get user choice
        while True:
            user_guess = input(
                "Do you think your number is higher or lower than the computer's?: "
            ).lower()
            if user_guess in ["higher", "lower"]:
                break
            else:
                user_guess = input("Please enter either higher or lower: ").lower()

        # Write game logic with points
        if user_guess == "higher" and user_number > computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif user_guess == "lower" and user_number < computer_number:
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        print(f"Your score is now {score}")

        if round_num < NUM_ROUNDS:
            print()

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
