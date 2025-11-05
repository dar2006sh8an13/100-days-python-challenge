#simple chatbot
while True:
    q = input("You: ").lower()
    if "hello" in q:
        print("Bot: Hello! How can I help?")
    elif "bye" in q:
        print("Bot: Bye 👋")
        break
    else:
        print("Bot: I don't understand")
