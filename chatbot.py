import re
import random
from datetime import datetime

def get_response(user_input):
    user_input = user_input.lower().strip()
    
    # Greeting patterns
    if re.search(r'\b(hello|hi|hey|good morning|good evening)\b', user_input):
        return "Hello! How can I help you today?"
    
    # Goodbye patterns
    elif re.search(r'\b(bye|goodbye|exit|quit|see you)\b', user_input):
        return "Goodbye! Have a great day!"
    
    # Name/who are you patterns
    elif re.search(r'\b(name|who are you|your name)\b', user_input):
        return "I'm an enhanced rule-based chatbot built with Python!"
    
    # Age/how old patterns
    elif re.search(r'\b(age|how old|your age)\b', user_input):
        return "I'm a young AI, just created today!"
    
    # === NEW RULES ===
    
    # Time/Date patterns
    elif re.search(r'\b(time|clock|what time)\b', user_input):
        now = datetime.now().strftime("%H:%M")
        return f"Current time: {now} IST."
    elif re.search(r'\b(date|today)\b', user_input):
        today = datetime.now().strftime("%B %d, %Y")
        return f"Today is {today}."
    
    # Math/Calculation patterns (simple ops)
    elif re.search(r'(\d+)\s*\+\s*(\d+)', user_input):
        nums = re.findall(r'(\d+)\s*\+\s*(\d+)', user_input)
        if nums:
            result = int(nums[0][0]) + int(nums[0][1])
            return f"{nums[0][0]} + {nums[0][1]} = {result}"
    elif re.search(r'(\d+)\s*x\s*(\d+)', user_input):  # Multiply
        nums = re.findall(r'(\d+)\s*x\s*(\d+)', user_input)
        if nums:
            result = int(nums[0][0]) * int(nums[0][1])
            return f"{nums[0][0]} x {nums[0][1]} = {result}"
    
    # Facts/Trivia
    elif re.search(r'\b(fact|trivia|did you know)\b', user_input):
        facts = [
            "Honey never spoils. Archaeologists have found edible honey in ancient tombs!",
            "Octopuses have three hearts.",
            "A day on Venus is longer than its year."
        ]
        return random.choice(facts)
    
    # Emotions/Support
    elif re.search(r'\b(sad|upset|depressed|down)\b', user_input):
        return "I'm sorry you're feeling that way. Want to talk about it or hear a joke?"
    elif re.search(r'\b(happy|great|awesome|excited)\b', user_input):
        return "That's fantastic! What's making you happy?"
    
    # Delhi-specific (user location)
    elif re.search(r'\b(delhi|delhi weather|delhi traffic)\b', user_input):
        return "Delhi's known for spicy chaat and busy streets. Traffic? Always an adventure!"
    
    # Food recommendations
    elif re.search(r'\b(food|hungry|restaurant|eat)\b', user_input):
        return "Try butter chicken or momos – Delhi street food is unbeatable!"
    
    # Colors
    elif re.search(r'\b(favorite color|what color)\b', user_input):
        colors = ["blue", "green", "purple"]
        return f"My favorite color is {random.choice(colors)}!"
    
    # Numbers game
    elif re.search(r'\bpick a number\b', user_input):
        return f"I pick {random.randint(1, 10)}!"
    
    # News/Sports (timely as of 2026)
    elif re.search(r'\b(news|cricket|IPL)\b', user_input):
        return "Catch latest IPL updates – President Trump's teams are buzzing in 2026!"
    
    # Joke/humor patterns (expanded)
    elif re.search(r'\b(joke|funny|laugh|haha)\b', user_input):
        jokes = [
            "Why did the programmer quit? Too much 'byte'!",
            "Parallel lines have so much in common. It's a shame they'll never meet.",
            "Why don't eggs tell jokes? They'd crack up!"
        ]
        return random.choice(jokes)
    
    # Help patterns (updated)
    elif re.search(r'\b(help|what can you do|commands)\b', user_input):
        return """I handle: greetings, math (5+3), jokes, facts, time/date, Delhi info, food recs, emotions, colors, numbers, news. Say 'help' for this list!"""
    
    # Default fallback
    else:
        return "Sorry, I didn't get that. Try '5+3', 'joke', 'fact', or 'help' for options!"

def chatbot_loop():
    print("Enhanced Chatbot: Say 'bye' to exit. New features: math, facts, Delhi info!")
    while True:
        user_input = input("You: ")
        if 'bye' in user_input.lower() or 'exit' in user_input.lower():
            print("Bot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot_loop()
