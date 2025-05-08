"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""


def main():
    # Fill this function out!

    # Prompt the user for their weight on Earth
    weight_earth = float(input("Enter a weight on Earth: "))

    # Calculate the weight on Mars
    weight_mars = weight_earth * 0.378

    # Print the result
    print(f"The equivalent weight on Mars: {weight_mars}")


if __name__ == "__main__":
    main()
