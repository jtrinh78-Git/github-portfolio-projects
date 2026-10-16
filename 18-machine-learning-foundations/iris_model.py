from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

iris = load_iris()

print(iris.data.shape)

print(iris.data[:5])

print(iris.target[:5])

print(iris.target_names)

X = iris.data

y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
print("Training flowers:", len(X_train))
print("Testing flowers:", len(X_test))

model = LogisticRegression(max_iter=200)

model.fit(X_train, y_train)

prediction = model.predict(X_test[:1])

print("Predicted species:", prediction)
print("Predicted flower name:", iris.target_names[prediction[0]])

print("Actual species:", y_test[:1])

accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.2%}")

predictions = model.predict(X_test)

print("ALL predictions:", predictions)
print("Actual answers:", y_test)

for i in range(len(y_test)):
    if predictions[i] != y_test[i]:
        print("Wrong flower index:", i)
        print("Flower measurements:", X_test[i])
        print("Species probabilities:", model.predict_proba(X_test[i:i+1]))