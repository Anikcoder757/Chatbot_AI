#CHATBOT WITH RULE-BASED RESPONSES

import re
def simple_chatbot(user_input):
    # Define rules and responses
    rules = {
        r'hello|hi|hey': 'Hello! How can I help you?',
        r'I am fine': 'Ohh Good!',
        r'how are you': 'I am a chatbot, so I don\'t have feelings, but thanks for asking!',
        r'bye|goodbye': 'Goodbye! Have a great day!',
        r'your name': 'I am a simple chatbot.',
        r'your age': 'I am just a program, so I don\'t have an age.',
        r'help': 'I can provide information or answer questions. Just ask me anything!',
        r'thank you': 'You\'re welcome! If you have more questions, feel free to ask.'
    }

    # Check user input against rules
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    # If no match is found
    return "I'm sorry, I don't understand that. Can you please rephrase or ask something else?"

# Main loop for interacting with the chatbot
print("Simple Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("User: ")
    if user_input.lower() == 'bye':
        print("Simple Chatbot: Goodbye!")
        break
    else:
        response = simple_chatbot(user_input)
        print("Simple Chatbot:", response)
