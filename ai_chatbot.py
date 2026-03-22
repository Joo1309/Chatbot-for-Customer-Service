import nltk
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')

sentences = [
    "hi", "hello", "hey",
    "how are you", "how are you doing",
    "refund", "money back",
    "where is my order", "track order",
    "bye", "goodbye"
]

labels = [
    "greeting", "greeting", "greeting",
    "status", "status",
    "refund", "refund",
    "order", "order",
    "bye", "bye"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

model = LogisticRegression()
model.fit(X, labels)

responses = {
    "greeting": ["Hello! 😊", "Hi there!", "Hey!"],
    "status": ["I'm doing great!", "All good here!"],
    "refund": ["Refund takes 5-7 days."],
    "order": ["Your order is on the way 🚚"],
    "bye": ["Goodbye! 👋"]
}

def get_response(user_input):
    X_test = vectorizer.transform([user_input])
    tag = model.predict(X_test)[0]
    return random.choice(responses[tag])