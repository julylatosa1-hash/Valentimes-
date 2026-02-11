import random
import time

# List of romantic messages
valentine_messages = [
    "Will you be my Valentine? 💖",
    "Roses are red, violets are blue, will you be my Valentine? 🌹",
    "You're the one for me! Be my Valentine? 😘",
    "Let's make this Valentine's Day special together! ❤️",
    "Be my Valentine and make my heart skip a beat! 💕"
]

# List of yes responses
yes_responses = [
    "Yay! I'm so happy! Let's celebrate! 🎉",
    "Awesome! You're the best! 💑",
    "My heart is yours! Happy Valentine's Day! 💖"
]

# List of no responses
no_responses = [
    "That's okay, friends forever! 😊",
    "No worries, maybe next time! 🌟",
    "I'll keep trying! 😉"
]

def be_my_valentine():
    print("AI Valentine Bot: Hi there! I'm here to ask something special...")
    time.sleep(1)

    message = random.choice(valentine_messages)
    print(f"AI Valentine Bot: {message}")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ['yes', 'y', 'sure', 'okay', 'absolutely']:
            response = random.choice(yes_responses)
            print(f"AI Valentine Bot: {response}")
            break
        elif user_input in ['no', 'n', 'sorry', 'maybe not']:
            response = random.choice(no_responses)
            print(f"AI Valentine Bot: {response}")
            break
        else:
            print("AI Valentine Bot: Hmm, I didn't catch that. Say 'yes' or 'no'? 😅")

if __name__ == "__main__":
    be_my_valentine()
