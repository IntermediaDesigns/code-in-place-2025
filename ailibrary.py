from ai import call_gpt


def main():

    # response = call_gpt()

    # response = input()

    print("Welcome to the AI Library!")
    print("This is a simple AI library that interacts with OpenAI's GPT-3.")
    print("You can ask me anything, and I'll do my best to provide a helpful response.")
    print("Type 'exit' to quit the program.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        else:
            response = call_gpt(user_input)
            print(f"AI: {response}")


if __name__ == "__main__":
    main()
