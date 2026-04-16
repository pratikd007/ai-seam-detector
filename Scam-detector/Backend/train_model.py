import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample dataset (you can expand later)
data = {
    "text": [
        # Scam messages
        "win money now",
        "free lottery offer",
        "urgent verify your bank account",
        "click here to claim prize",
        "you won cash reward",
        "free recharge click now",
        "your account blocked verify otp",
        "limited offer click fast",
        "get money instantly",
        "claim your free gift card",

        # Safe messages
        "hello how are you",
        "let's meet tomorrow",
        "project meeting at 5pm",
        "happy birthday bro",
        "see you at class",
        "call me later",
        "thanks for your help",
        "good morning",
        "are you coming today",
        "let's study together"
    ],
    "label": [
        1,1,1,1,1,1,1,1,1,1,  # scam
        0,0,0,0,0,0,0,0,0,0   # safe
    ]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])

model = MultinomialNB()
model.fit(X, df["label"])

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained & saved!")