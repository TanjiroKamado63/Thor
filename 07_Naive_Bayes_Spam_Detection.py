# Practical 7: Spam Detection using Naive Bayes
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

corpus = [
    "Get rich quick! Click here now!",
    "Hey, are we still meeting for lunch today?",
    "Free cash prize! Claim your reward.",
    "Can you send me the project report?",
    "Urgent: Account suspended. Verification required.",
    "Don't forget to buy milk on your way home.",
]
labels = [1, 0, 1, 0, 1, 0]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
y = labels

model = MultinomialNB()
model.fit(X, y)

test_emails = [
    "Hey buddy, let's grab a coffee later.",
    "CONGRATULATIONS! You won a free vacation! Click now",
]

X_test = vectorizer.transform(test_emails)
predictions = model.predict(X_test)

for email, pred in zip(test_emails, predictions):
    status = "SPAM" if pred == 1 else "HAM (Safe)"
    print(f"Email: '{email}' --> Predicted as: {status}")
