from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X = [[1], [2], [3], [4], [5], [6], [7], [8]]   # hours student study

y = [0, 0, 0, 0, 1, 1, 1, 1]   # fail or pass

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

model = LogisticRegression()

model.fit(X_train, y_train)

prediction = model.predict([[6]])

print(prediction)

probability = model.predict_proba([[6]])

print(probability)

accuracy = model.score(X_test, y_test)

print(accuracy)

print(X_test)
print(y_test)