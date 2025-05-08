"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then
prints the equivalent weight on that planet.

Note that the user should type in a planet with
the first letter as uppercase, and you do not need
to handle the case where a user types in something
other than one of the planets (that is not Earth).

$ python planetaryweight.py

Enter a weight on Earth: 120

Enter a planet: Mars

The equivalent weight on Mars: 45.36

"""


def main():
    # Fill this function out!
    # Prompt the user for their weight on Earth
    weight_earth = float(input("Enter a weight on Earth: "))

    # Prompt the user for a planet
    planet = input("Enter a planet: ")

    # Initialize the weight on the planet
    weight_planet = 0.0

    # Calculate the weight on the planet based on the input
    if planet == "Mercury":
        weight_planet = weight_earth * 0.376
    elif planet == "Venus":
        weight_planet = weight_earth * 0.889
    elif planet == "Mars":
        weight_planet = weight_earth * 0.378
    elif planet == "Jupiter":
        weight_planet = weight_earth * 2.36
    elif planet == "Saturn":
        weight_planet = weight_earth * 1.081
    elif planet == "Uranus":
        weight_planet = weight_earth * 0.815
    elif planet == "Neptune":
        weight_planet = weight_earth * 1.14
    else:
        print("Unknown planet")
        return

    # Round the value to 2 decimal places before printing
    weight_planet = round(weight_planet, 2)

    # Print the result
    print(f"The equivalent weight on {planet}: {weight_planet}")


if __name__ == "__main__":
    main()
