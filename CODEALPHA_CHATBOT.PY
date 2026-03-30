def chatbot():

    print("🤖 Simple Chatbot")
    print("Type 'bye' to exit\n")

    bot_name = "Alex" # Initialize bot_name

    while True:

        user_input = input("You: ").lower()

        if user_input in ["hello", "hi"]:
            print("Bot: Hello! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")

        elif user_input == "your name":
            print(f"Bot: My name is {bot_name} and I am a Python chatbot.") # Use bot_name

        elif user_input == "help":
            print("Bot: You can say hello, ask how I am, or say bye.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()