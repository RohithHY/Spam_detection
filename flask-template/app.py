import os
import pickle
import re
from flask import Flask, render_template, request

app = Flask(__name__)

# Load model and vectorizer
MODEL_PATH = os.path.join("model", "spam_model.pkl")
VECTORIZER_PATH = os.path.join("model", "vectorizer.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
with open(VECTORIZER_PATH, "rb") as f:
    vectorizer = pickle.load(f)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.strip()
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        message = request.form.get("message", "")
        cleaned_message = clean_text(message)
        if cleaned_message:
            msg_vec = vectorizer.transform([cleaned_message])
            pred = model.predict(msg_vec)[0]
            prediction = "Spam" if pred == 1 else "Not Spam"
    return render_template("index.html", prediction=prediction)

@app.route("/predict", methods=["POST"])
def predict():
    message = request.form.get("message", "")
    cleaned_message = clean_text(message)
    prediction = None
    if cleaned_message:
        msg_vec = vectorizer.transform([cleaned_message])
        pred = model.predict(msg_vec)[0]
        prediction = "Spam" if pred == 1 else "Not Spam"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)