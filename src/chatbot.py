from predict import predict_emotion


# =========================================================
# RESPONSE DICTIONARY
# =========================================================

responses = {

    "sadness":
        "I'm here for you. Things can improve.",

    "joy":
        "That's wonderful to hear!",

    "anger":
        "Take a moment to breathe calmly.",

    "fear":
        "You are safe. Try grounding yourself.",

    "love":
        "Connection and care are important."
}


# =========================================================
# CHATBOT RESPONSE FUNCTION
# =========================================================

def chatbot_response(text):

    # PREDICT EMOTION
    emotion = predict_emotion(text)

    # GET RESPONSE
    response = responses.get(
        emotion,
        "I understand your feelings."
    )

    return emotion, response


# =========================================================
# TEST
# =========================================================

user_input = "I feel lonely and upset"

emotion, reply = chatbot_response(user_input)

print("Detected Emotion:", emotion)
print("Chatbot Response:", reply)