import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

def chatbot_response(user_input):
    doc = nlp(user_input.lower())

    # Check for greetings
    for token in doc:
        if token.text in ["hi", "hello", "hey"]:
            return "Hello! How can I assist you?"
        if token.text == "bye":
            return "Goodbye! Have a nice day!"

    # Default response
    return "I'm still learning. Can you rephrase?"

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot_response(user_input))













# import random

# def chatbot_response(user_input):
#     responses = {
#         "hello": "Hi there! How can I help you?",
#         "hi": "Hello! What’s up?",
#         "bye": "Goodbye! Have a great day!",
#         "your name": "I'm a chatbot built with Python!"
#     }
    
#     for key in responses:
#         if key in user_input.lower():
#             return responses[key]
    
#     return random.choice([
#         "I'm not sure how to answer that.",
#         "Can you rephrase?",
#         "Interesting! Tell me more."
#     ])

# print("Chatbot: Hello! Type 'bye' to exit.")

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "bye":
#         print("Chatbot: Goodbye!")
#         break
#     print("Chatbot:", chatbot_response(user_input))
