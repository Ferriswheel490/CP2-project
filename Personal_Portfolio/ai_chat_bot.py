import random

def chat():
    print("""
This is a short AI chatbot.
There's a bit to do, and I made this on short notice.
""")
    ans = input("Do you want to use it? (y/n): ").lower()  # Make input case insensitive
    if ans == "yes" or ans == "y":
        ai_chat()
    elif ans == "no" or ans == "n":
        print("Goodbye! Returning to the main menu...")
        return  # Exiting the chatbot (or you can call a main menu function here)
    else:
        print("Please answer with 'yes' or 'no'.")
        chat()  # Repeat the question if the answer isn't valid

# Define a dictionary of patterns and responses
responses = {
    "hello": ["Hi!", "Hello there!", "Hey!", "Greetings!"],
    "how are you": ["I'm doing great, thanks for asking!", "I'm just a bot, but I'm fine!", "I'm doing well, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye! Come back soon!"],
    "default": ["Sorry, I didn't understand that.", "Can you please rephrase?", "I'm not sure what you mean."]
}

# Function to get response based on user input
def get_response(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check for a matching response or return a default one
    for pattern in responses:
        if pattern in user_input:
            return random.choice(responses[pattern])

    return random.choice(responses["default"])

# Main chatbot function
def ai_chat():
    print("Welcome to the AI Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("AI Chatbot: Goodbye! Take care!")
            break
        else:
            response = get_response(user_input)
            print(f"AI Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chat()
