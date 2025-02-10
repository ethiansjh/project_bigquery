#!/usr/bin/env python
# coding: utf-8

import pandas as pd
df = pd.read_csv('/Users/amandinedeseptenville/code/Tronyque/spaceship_titanic/spaceship-titanic/train.csv', delimiter=',')

df.drop(columns=['PassengerId'], inplace=True)

df['Transported'] = df['Transported'].astype(int)

# Remplacer les valeurs manquantes par le mode
for column in ['HomePlanet', 'CryoSleep', 'Destination', 'VIP']:
    df[column].fillna(df[column].mode()[0], inplace=True)

for column in ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']:
    df[column].fillna(df[column].median(), inplace=True)

# Split the 'Cabin' column into three new columns: 'Deck', 'Num', and 'Side'
df[['Deck', 'Num', 'Side']] = df['Cabin'].str.split('/', expand=True)

df['totalspent'] = df[['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']].sum(axis=1)

df['HasSpent'] = df['totalspent'] > 0
df.head()

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


df.drop(columns=['Name'], inplace=True)

df.dropna(inplace=True)

from sklearn.preprocessing import StandardScaler

# Initialize the StandardScaler
scaler = StandardScaler()

# Select the numerical columns to scale
numerical_columns = ['Age', 'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck', 'totalspent']

# Apply the scaler to the numerical columns
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

df['Num'] = df['Num'].astype(int)





