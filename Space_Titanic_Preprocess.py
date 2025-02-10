#!/usr/bin/env python
# coding: utf-8

import pandas as pd
df = pd.read_csv('/Users/amandinedeseptenville/code/Tronyque/spaceship_titanic/spaceship-titanic/train.csv', delimiter=',')


df.drop(columns=['PassengerId'], inplace=True)
df.head()


df['Transported'] = df['Transported'].astype(int)

df.nunique()

# Remplacer les valeurs manquantes par le mode
for column in ['HomePlanet', 'CryoSleep', 'Destination', 'VIP']:
    df[column].fillna(df[column].mode()[0], inplace=True)


for column in ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']:
    df[column].fillna(df[column].median(), inplace=True)


# Split the 'Cabin' column into three new columns: 'Deck', 'Num', and 'Side'
df[['Deck', 'Num', 'Side']] = df['Cabin'].str.split('/', expand=True)


df['totalspent'] = df[['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']].sum(axis=1)

df['HasSpent'] = df['totalspent'] > 0

df['CabinShared'] = df.duplicated(subset=['Num'], keep=False)

df = pd.get_dummies(df, columns=['HomePlanet', 'Destination', 'Deck', 'Side'])



from sklearn.preprocessing import LabelEncoder

# Initialize the LabelEncoder
le = LabelEncoder()

# Apply label encoding to the 'CryoSleep' and 'VIP' columns
df['CryoSleep'] = le.fit_transform(df['CryoSleep'])
df['VIP'] = le.fit_transform(df['VIP'])


df.drop(columns=['Cabin'], inplace=True)

# Transform boolean columns to integers
bool_columns = df.select_dtypes(include='bool').columns
df[bool_columns] = df[bool_columns].astype(int)

df.head()

df.drop(columns=['Name'], inplace=True)

df.dropna(inplace=True)


from sklearn.preprocessing import StandardScaler

# Initialize the StandardScaler
scaler = StandardScaler()

# Select the numerical columns to scale
numerical_columns = ['Age', 'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck', 'totalspent']

# Apply the scaler to the numerical columns
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

df.head()


df['Num'] = df['Num'].astype(int)
df.head()


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
