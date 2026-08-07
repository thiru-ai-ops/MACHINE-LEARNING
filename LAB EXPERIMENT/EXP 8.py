from sklearn.linear_model import LinearRegression
X = [[1], [2], [3], [4], [5]]
y = [18, 25, 30, 36, 42]
model = LinearRegression()
model.fit(X, y)
pred = model.predict(X)
print("Actual Attendance (in thousands):", y)
print("Predicted Attendance (in thousands):", pred)
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
