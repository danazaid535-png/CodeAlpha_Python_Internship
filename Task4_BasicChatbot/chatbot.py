print("🤖 Welcome to the Basic Chatbot!")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! How are you?")
    elif user == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")
    elif user == "what is your name":
        print("Bot: My name is CodeAlpha Bot.")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
