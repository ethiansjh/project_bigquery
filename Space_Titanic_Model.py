#!/usr/bin/env python
# coding: utf-8


from sklearn.metrics import accuracy_score, mean_squared_error

# Initialize the RandomForestRegressor with the best parameters
best_rf = RandomForestRegressor(
    bootstrap=True,
    max_depth=None,
    min_samples_leaf=4,
    min_samples_split=10,
    n_estimators=300,
    random_state=42
)

# Fit the model to the training data
best_rf.fit(X_train, y_train)

# Predict on the test data
rf_best_predictions = best_rf.predict(X_test)

# Convert predictions to binary
rf_best_predictions_binary = (rf_best_predictions > 0.5).astype(int)

# Evaluate the model

rf_best_accuracy = accuracy_score(y_test, rf_best_predictions_binary)
rf_best_mse = mean_squared_error(y_test, rf_best_predictions)

print("Random Forest Best Model Accuracy: ", rf_best_accuracy)
print("Random Forest Best Model MSE: ", rf_best_mse)



# Display the results for the training dataset
print("Training Results:")
print("Random Forest Training Accuracy: ", rf_best_accuracy)
print("Random Forest Training Predictions: ", rf_best_predictions_binary)

# Display the results for the test dataset
print("\nTest Results:")
print("Random Forest Test Accuracy: ", rf_best_accuracy)
print("Random Forest Test Predictions: ", rf_best_predictions_binary)

