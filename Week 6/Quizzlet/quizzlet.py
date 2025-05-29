def main():
    # Dictionary of English words and their Spanish translations
    vocabulary = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo",
    }

    correct_count = 0
    total_questions = len(vocabulary)

    # Loop through each word in the dictionary
    for english_word, spanish_translation in vocabulary.items():
        # Ask the user for the translation
        user_answer = input(f"What is the Spanish translation for {english_word}? ")

        # Check if the answer is correct (case-insensitive)
        if user_answer.lower() == spanish_translation.lower():
            print("That is correct!")
            correct_count += 1
        else:
            print(
                f"That is incorrect, the Spanish translation for {english_word} is {spanish_translation}."
            )

        # Add blank line for visual clarity
        print()

    # Display final results
    print(
        f"You got {correct_count}/{total_questions} words correct, come study again soon!"
    )


if __name__ == "__main__":
    main()
