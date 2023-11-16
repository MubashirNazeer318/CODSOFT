import re

def simple_chatbot(user_input):
    # Define predefined rules and responses
    rules = {
        r'hello|hi|hey': 'Hello! How can I help you?',
        r'how are you': 'I am a bot, so I don\'t have feelings, but thanks for asking!',
        r'your name': 'I am a chatbot, you can call me Atlas.',
        r'bye|goodbye': 'Goodbye! Have a great day!',
        r'\b(?:thanks|thank you)\b': 'You\'re welcome!',
        r'.*': 'I didn\'t understand that. Can you please make the question clear or ask something else?'
    }

    # Check user input against rules and provide appropriate response
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

# Main loop for user interaction
print("Simple Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("User: ")
    if user_input.lower() == 'bye':
        print("Simple Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Simple Chatbot:", response)
