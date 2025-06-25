import json
import pickle
import random

# Load intents
with open("intents.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Load trained model and vectorizer
with open("model/trained_model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

# Predict intent & generate response
def get_response(user_input):
    user_input = user_input.lower()
    X_test = vectorizer.transform([user_input])
    predicted_tag = model.predict(X_test)[0]

    for intent in data["intents"]:
        if intent["tag"] == predicted_tag:
            return random.choice(intent["responses"])

    return "Maaf kijiye, mujhe samajh nahi aaya."
