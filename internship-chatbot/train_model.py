import json
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load intents
with open("intents.json", "r", encoding="utf-8") as f:
    data = json.load(f)

corpus = []
labels = []

# Build training data
for intent in data["intents"]:
    for pattern in intent["patterns"]:
        corpus.append(pattern.lower())
        labels.append(intent["tag"])

# Vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Save model and vectorizer
with open("model/trained_model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("✅ Model trained and saved to model/trained_model.pkl")
