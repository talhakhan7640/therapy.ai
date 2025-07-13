
def get_ai_response(user_message: str):
    if "sad" in user_message.lower():
        return "I'm sorry to hear that. Would you like to talk about it?"
    else:
        return "Thank you for sharing, How are you feeling now?"
