import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset (XOR problem)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Output labels
y = np.array([[0],
              [1],
              [1],
              [0]])

# Initialize weights and biases
np.random.seed(1)
input_layer_neurons = 2
hidden_layer_neurons = 3
output_neurons = 1

weights_input_hidden = np.random.rand(input_layer_neurons, hidden_layer_neurons)
weights_hidden_output = np.random.rand(hidden_layer_neurons, output_neurons)

bias_hidden = np.random.rand(1, hidden_layer_neurons)
bias_output = np.random.rand(1, output_neurons)

# Training the network
learning_rate = 0.1
epochs = 10000

for _ in range(epochs):
    # ---- Feed Forward ----
    hidden_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
    predicted_output = sigmoid(final_input)

    # ---- Backpropagation ----
    error = y - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden = d_predicted_output.dot(weights_hidden_output.T)
    d_hidden_output = error_hidden * sigmoid_derivative(hidden_output)

    # ---- Update weights and biases ----
    weights_hidden_output += hidden_output.T.dot(d_predicted_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_output) * learning_rate

    bias_output += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    bias_hidden += np.sum(d_hidden_output, axis=0, keepdims=True) * learning_rate

# Final output
print("Predicted Output after training:")
print(predicted_output)
