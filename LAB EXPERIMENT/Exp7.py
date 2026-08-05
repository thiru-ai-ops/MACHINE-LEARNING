from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
X = [
    [20, 2],
    [18, 3],
    [15, 5],
    [12, 6],
    [10, 8],
    [8, 10],
    [6, 12],
    [4, 15],
    [25, 1],
    [5, 14],
    [16, 4],
    [9, 9]
]
y = [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Actual Values:")
print(y_test)
print("\nPredicted Values:")
print(y_pred)
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nAccuracy:")
print(accuracy_score(y_test, y_pred) * 100, "%")
