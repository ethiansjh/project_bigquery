import pandas as pd
import pickle

df = pd.read_csv('data/Spaceship_Titanic_Preprocessed.csv')
from sklearn.model_selection import train_test_split

# Define the features and target variable
X = df.drop('Transported', axis=1)
y = df['Transported']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training and testing data split completed.")
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.ensemble import RandomForestRegressor

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

# Enregistrer le modèle dans un fichier pickle
print("Exporting model...")
with open('data/model.pkl', 'wb') as file:
    pickle.dump(best_rf, file)