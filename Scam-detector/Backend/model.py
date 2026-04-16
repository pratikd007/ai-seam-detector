import pickle

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def detect_scam(text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]

    result = "SCAM" if prediction == 1 else "SAFE"

    return {
    "result": result,
    "score": int(probability * 100),
    "confidence": f"{int(probability * 100)}% chance this is scam based on patterns"
}