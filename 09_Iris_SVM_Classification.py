# Practical 9: Iris Classification using SVM
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df["target"] = iris.target

print("--- Step A: Dataset Loaded ---")
print(df.head(), "\n")

X = df.drop(columns=["target"])
y = df["target"]
X = X.fillna(X.mean())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("--- Step B: Preprocessing Complete ---")
print(f"Sample scaled feature row: {X_scaled[0]}\n")

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

print("--- Step C: Dataset Split ---")
print(f"Training set size: {X_train.shape[0]} samples")
print(f"Testing set size: {X_test.shape[0]} samples\n")

classifier = SVC(kernel="linear", random_state=42)
classifier.fit(X_train, y_train)

print("--- Step D: Model Training Complete ---\n")

y_train_pred = classifier.predict(X_train)
y_test_pred = classifier.predict(X_test)
train_accuracy = accuracy_score(y_train, y_train_pred)
test_accuracy = accuracy_score(y_test, y_test_pred)

print("--- Step E: Final Results ---")
print(f"Training Accuracy: {train_accuracy * 100:.2f}%")
print(f"Testing Accuracy: {test_accuracy * 100:.2f}%")
