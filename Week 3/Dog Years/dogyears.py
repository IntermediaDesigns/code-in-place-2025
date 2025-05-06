# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18


def main():
    # On average every calendar year is equal to 7.18 dog years. To convert 3 calendar years to dog years, you multiply 3 * 7.18 to get 21.54 dog years.
    # Prompt the user for their age in years
    age = input("Enter an age in calendar years: ")

    # Convert the age to a float
    age = float(age)

    # Calculate the age in dog years
    dog_years = age * DOG_YEARS_MULTIPLIER

    # Round the dog years to 2 decimal places
    dog_years = round(dog_years, 2)

    # Print the age in dog years
    print(f"That's {dog_years} in dog years!")


# There is no need to edit code beyond this point
if __name__ == "__main__":
    main()
