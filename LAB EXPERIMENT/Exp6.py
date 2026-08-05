from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
X = [
    [19,19000],
    [22,25000],
    [25,35000],
    [28,40000],
    [30,50000],
    [35,65000],
    [40,80000],
    [42,90000],
    [45,100000],
    [48,120000],
    [50,130000],
    [55,150000]
]
y = [0,0,0,0,0,1,1,1,1,1,1,1]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
model = GaussianNB()
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
