import random 
import re
from datetime import datetime

# CHATBOT KNOWLEDGE BASE

knowledge_base = {
    "python": (
        "Python is a high-level programming language known "
        "for its simple syntax. It is used in AI, data science, "
        "automation, web development, and many other fields."
    ),

    "artificial intelligence": (
        "Artificial Intelligence (AI) is a field of computer "
        "science that focuses on building systems capable of "
        "performing tasks that normally require human intelligence."
    ),

    "machine learning": (
        "Machine Learning is a branch of AI that enables computers "
        "to learn patterns from data and make predictions or decisions."
    ),

    "data science": (
        "Data Science combines statistics, programming, and domain "
        "knowledge to extract useful insights from data."
    ),

    "computer": (
        "A computer is an electronic device that accepts data, "
        "processes it according to instructions, and produces output."
    ),

    "database": (
        "A database is an organized collection of data that can "
        "be stored, managed, retrieved, and updated efficiently."
    ),

    "internet": (
        "The Internet is a global network of connected computers "
        "and devices that communicate using standard protocols."
    )
}

# CHATBOT RESPONSE

responses = {
    "greeting": [
        "Hello! How can I help you today?",
        "Hi there! What would you like to talk about?",
        "Hey! I'm ready to chat with you."
    ],

    "how_are_you": [
        "I'm functioning properly and ready to help!",
        "I'm doing well! What can I help you with?",
        "All good here! Tell me what's on your mind."
    ],

    "thanks": [
        "You're welcome!",
        "Happy to help!",
        "Anytime! Let me know if you need anything else."
    ],

    "goodbye": [
        "Goodbye! Have a wonderful day!",
        "See you later! Take care.",
        "Bye! It was nice chatting with you."
    ]
}

# CONVERSATIION MEMORY

user_name = None
conversation_history = []

# DISPLAY HELP

def show_help():

    print("""
Here are some things you can ask me:

1. Greetings:
   Hello, Hi, Good morning

2. General conversation:
   How are you?
   Who are you?
   What can you do?

3. Knowledge:
   Explain Python
   What is Artificial Intelligence?
   What is Machine Learning?
   What is Data Science?
   Explain databases

4. Mathematics:
   Calculate 25 + 15
   What is 100 / 4?
   Calculate 12 * 8

5. Date and time:
   What is today's date?
   What time is it?

6. Memory:
   My name is Maurvika
   What is my name?

7. Other commands:
   History
   Help
   Bye
""")

# MATHEMATICAL CALCULATOR 

def calculate(message):

    # Find a simple arithmetic expression
    pattern = (
        r"(?:calculate\s+|what\s+is\s+)?"
        r"(-?\d+(?:\.\d+)?)\s*"
        r"([+\-*/])\s*"
        r"(-?\d+(?:\.\d+)?)"
        r"\s*\??"
    )

    match = re.search(pattern, message)

    if not match:
        return None

    number1 = float(match.group(1))
    operator = match.group(2)
    number2 = float(match.group(3))

    if operator == "+":
        result = number1 + number2

    elif operator == "-":
        result = number1 - number2

    elif operator == "*":
        result = number1 * number2

    elif operator == "/":

        if number2 == 0:
            return "Division by zero is not allowed."

        result = number1 / number2

    # Display integers without unnecessary decimal places
    if result.is_integer():
        result = int(result)

    return f"The answer is {result}."

# GENERATE CHATBOT RESPONSE

def get_response(message):

    global user_name

    # Normalize the message
    message = message.lower().strip()

    # Save the conversation
    conversation_history.append(("You", message))

# EMPTY INPUT

    if not message:
        return "Please type something so we can chat."

 # EXIT COMMANDS  

    if message in ["bye", "goodbye", "exit", "quit"]:
        return random.choice(responses["goodbye"])

# GREETING DETECTION    

    if re.search(
        r"\b(hello|hi|hey|good morning|good afternoon|good evening)\b",
        message
    ):
        return random.choice(responses["greeting"])

# HOW ARE YOU ?

    if re.search(r"\bhow are you\b", message):
        return random.choice(responses["how_are_you"])

# THANK-YOU MESSAGES

    if re.search(r"\b(thanks|thank you|thx)\b", message):
        return random.choice(responses["thanks"])

# REMEMBER USER'S NAME 

    name_match = re.search(
        r"\bmy name is\s+([a-zA-Z]+)\b",
        message
    )

    if name_match:

        user_name = name_match.group(1).capitalize()

        return f"Nice to meet you, {user_name}!"

# RECALL USER'S NAME 

    if re.search(
        r"\b(what is my name|do you know my name|remember my name)\b",
        message
    ):

        if user_name:
            return f"Your name is {user_name}."

        return "You haven't told me your name yet."

# CURRENT DATA AND TIME

    if re.search(r"\b(date|today's date|today is)\b", message):

        current_date = datetime.now().strftime("%d %B %Y")

        return f"Today's date is {current_date}."

    if re.search(r"\b(time|current time)\b", message):

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}."

# CALCULATOR

    if re.search(
        r"\b(calculate|what is|how much is)\b",
        message
    ) or re.fullmatch(
        r"\s*-?\d+(?:\.\d+)?\s*[+\-*/]\s*-?\d+(?:\.\d+)?\s*\??\s*",
        message
    ):

        answer = calculate(message)

        if answer is not None:
            return answer

# HELP COMMAND 

    if message in ["help", "commands", "what can you do"]:

        show_help()

        return "These are the features I currently support."

# CONVERSATION HISTORY

    if message in ["history", "show history", "chat history"]:

        if len(conversation_history) <= 1:
            return "There isn't much conversation history yet."

        history_text = "\n".join(
            f"{speaker}: {text}"
            for speaker, text in conversation_history[:-1]
        )

        return "Here is our conversation history:\n" + history_text

# IDENTITY

    if re.search(r"\b(who are you|your name)\b", message):

        return (
            "I'm PyBot, a Python-based rule-driven chatbot. "
            "I can chat, perform basic calculations, "
            "remember your name during this session, "
            "and answer questions from my knowledge base."
        )

# SEARCH THE KNOWLEDGE BASE

    for topic, answer in knowledge_base.items():

        if topic in message:

            return answer

# UNKNOWN QUESTIONS

    return (
        "I'm not sure how to answer that yet. "
        "Try asking about Python, AI, Machine Learning, "
        "Data Science, computers, or databases. "
        "You can also type 'help' to see my capabilities."
    ) 

# MAIN CHAT LOOP

def main():

    print("-" * 50)
    print("    WELCOME TO PYBOT - YOUR CHATBOT FRIEND")
    print("-" * 50)

    print("Your personal Python - based chatbot!")
    print("Type 'help' to see available features.")
    print("Type 'bye' to end the conversation.")

    while True:

        user_message = input("\n You:")

        response = get_response(user_message)

        print("\nPyBot:", response)

        conversation_history.append(("PyBot", response))

        # Exit the loop if the user says goodbye

        if user_message.lower().strip() in [
            "bye", "goodbye", "exit", "quit"
        ]:
            break

    print("\nChat session ended. Thank you for chatting with PyBot!!")

# START THE PROGRAM

if __name__ == "__main__":
    main()


