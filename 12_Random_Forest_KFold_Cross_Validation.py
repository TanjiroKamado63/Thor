# Practical 12: K-Fold Cross-Validation using Random Forest
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_score

iris = load_iris()
X, y = iris.data, iris.target

model = RandomForestClassifier(random_state=42)
kf = KFold(n_splits=5, shuffle=True, random_state=42)

scores = cross_val_score(model, X, y, cv=kf, scoring="accuracy")

print("--- 5-Fold Cross-Validation Results ---")
for fold_idx, score in enumerate(scores, 1):
    print(f"Fold {fold_idx} Accuracy: {score * 100:.2f}%")

print("-" * 38)
print(f"Mean Accuracy: {scores.mean() * 100:.2f}%")
print(f"Std Deviation: {scores.std() * 100:.2f}%")
