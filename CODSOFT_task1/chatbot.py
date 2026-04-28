# ==========================================
# Simple Rule-Based Chatbot
# ==========================================

import re

# I'm using a 'state' variable to keep track of where we are in a conversation
# This helps the bot remember if it just asked the user a question.
bot_state = "normal"

def get_response(text):
    global bot_state
    
    # Cleaning the input so "Hello" and "hello " both work
    msg = text.lower().strip()

    # --- THE HELP FLOW ---
    # If the bot asked what kind of help they need, we check the answer here
    if bot_state == "waiting_for_help_type":
        if "1" in msg or "tech" in msg:
            bot_state = "normal"
            return "Got it. For tech stuff, I recommend checking out the Python docs!"
        elif "2" in msg or "general" in msg:
            bot_state = "normal"
            return "This is a Task 1 project for my CodSoft internship. It uses Regex!"
        else:
            return "I didn't get that. Please type '1' for Tech or '2' for General."

    # --- BASIC RULES ---
    
    # Simple greetings
    if re.search(r'\b(hi|hello|hey|yo)\b', msg):
        return "Hey! Hope you're having a good day. How can I help?"

    # Identity check
    if "who are you" in msg or "your name" in msg:
        return "I'm a rule-based chatbot."

    # Starting the multi-turn flow
    if msg == "help":
        bot_state = "waiting_for_help_type"
        return "Sure thing! What do you need help with?\n1. Tech/Code\n2. General Info"

    # Explaining NLP
    if "nlp" in msg:
        return "NLP stands for Natural Language Processing. It's basically how I'm reading your text right now!"

    # Small talk
    if "how are you" in msg:
        return "I'm just a script, so I'm doing great! How about you?"

    # Closing the chat
    if "bye" in msg or "exit" in msg:
        return "Alright, see ya later!"

    # Default fallback
    return "I'm not quite sure what you mean by that... try asking for 'help'."

# Main loop to run the program
def main():
    print("--- CHATBOT STARTING ---")
    print("(type 'exit' to stop the program)")
    
    while True:
        user_input = input("Me: ")
        
        # If user wants to quit
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Bot: Goodbye!")
            break
            
        answer = get_response(user_input)
        print("Bot:", answer)

if __name__ == "__main__":
    main()