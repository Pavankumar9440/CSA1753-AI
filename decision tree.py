from sklearn.tree import DecisionTreeClassifier

# Training data
# Features: [Age, Income]
X = [
    [25, 50000],
    [30, 60000],
    [45, 80000],
    [35, 65000],
    [50, 90000]
]

# Target labels
Y = ['No', 'No', 'Yes', 'No', 'Yes']

# Create Decision Tree model
model = DecisionTreeClassifier()

# Train the model
model.fit(X, Y)

# Test data
test = [[40, 70000]]

# Prediction
result = model.predict(test)

print("Prediction:", result)
