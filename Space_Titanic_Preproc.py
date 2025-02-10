#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('/Users/amandinedeseptenville/code/Tronyque/spaceship_titanic/spaceship-titanic/train.csv', delimiter=',')
df.head()


# In[2]:


df.info()


# In[3]:


df.drop(columns=['PassengerId'], inplace=True)
df.head()


# In[8]:


df['Transported'] = df['Transported'].astype(int)
df.head()


# In[9]:


df.nunique()


# In[10]:


# Remplacer les valeurs manquantes par le mode
for column in ['HomePlanet', 'CryoSleep', 'Destination', 'VIP']:
    df[column].fillna(df[column].mode()[0], inplace=True)

df.head()


# In[11]:


for column in ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']:
    df[column].fillna(df[column].median(), inplace=True)

df.head()


# In[12]:


# Split the 'Cabin' column into three new columns: 'Deck', 'Num', and 'Side'
df[['Deck', 'Num', 'Side']] = df['Cabin'].str.split('/', expand=True)

# Display the first few rows to verify the changes
df.head()


# In[13]:


df['totalspent'] = df[['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck']].sum(axis=1)
df.head()


# In[14]:


df['HasSpent'] = df['totalspent'] > 0
df.head()


# In[15]:


df['CabinShared'] = df.duplicated(subset=['Num'], keep=False)
df.head()


# In[16]:


df = pd.get_dummies(df, columns=['HomePlanet', 'Destination', 'Deck', 'Side'])
df.head()


# In[17]:


from sklearn.preprocessing import LabelEncoder

# Initialize the LabelEncoder
le = LabelEncoder()

# Apply label encoding to the 'CryoSleep' and 'VIP' columns
df['CryoSleep'] = le.fit_transform(df['CryoSleep'])
df['VIP'] = le.fit_transform(df['VIP'])

df.head()


# In[18]:


df.drop(columns=['Cabin'], inplace=True)
df.head()


# In[19]:


# Transform boolean columns to integers
bool_columns = df.select_dtypes(include='bool').columns
df[bool_columns] = df[bool_columns].astype(int)

df.head()


# In[20]:


df.drop(columns=['Name'], inplace=True)
df.head()


# In[21]:


df.info()


# In[22]:


df.dropna(inplace=True)
df.head()


# In[23]:


df.info()


# In[24]:


df.head()


# In[25]:


from sklearn.preprocessing import StandardScaler

# Initialize the StandardScaler
scaler = StandardScaler()

# Select the numerical columns to scale
numerical_columns = ['Age', 'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck', 'totalspent']

# Apply the scaler to the numerical columns
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

df.head()


# In[26]:


df['Num'] = df['Num'].astype(int)
df.head()


# In[27]:


df.info()


# In[28]:


df.to_csv('preprocessed_data.csv', index=False)


# In[ ]:




