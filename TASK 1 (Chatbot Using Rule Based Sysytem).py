# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 20:15:13 2024

@author: rajra
"""

class RuleBasedChatbot:
    def respond(self, message):
        message = message.lower()
        if "hi" in message:
            return "Hello! How can I help you today?"
        elif "how are you" in message:
            return "I'm good,and hope you also will be fine!"
        elif "what is your name" in message:
            return "I'm a rule-based chatbot!"
        elif "i love you" in message:
            return"i love  you too!"
        elif"today's weather condition" in message:
            return"weather is good "
        elif "bye" in message:
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Instantiate the chatbot
chatbot = RuleBasedChatbot()
x=str(input("Write your good name:-"))

# Start the conversation loop
print("Rule-based Chatbot: Hello! How can I help you today?")
while True:
    user_input = input(x).strip()
    if user_input.lower() == 'bye':
        print("Rule-based Chatbot:", chatbot.respond(user_input))
        break
    print("Rule-based Chatbot:", chatbot.respond(user_input))
