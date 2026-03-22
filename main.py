while True:
    user = input("You: ").lower()

    if user == "hi":
        print("Bot: Hello! 😊")

    elif user == "how are you":
        print("Bot: I'm doing great! How can I help you?")

    elif user == "help":
        print("Bot: I can help you with orders, refunds, and contact info.")

    elif user == "order":
        print("Bot: Your order is on the way 🚚")

    elif user == "refund":
        print("Bot: Refund takes 5-7 working days.")

    elif user == "contact":
        print("Bot: You can contact us at support@example.com")

    elif user == "price":
        print("Bot: Prices vary depending on the product.")

    elif user == "bye":
        print("Bot: Goodbye! 👋")
        break

    else:
        print("Bot: I don't understand, try something else.")