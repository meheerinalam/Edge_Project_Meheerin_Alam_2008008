# -*- coding: utf-8 -*-
"""EEG_signal_emotion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12B87vmFmmrvEMFy9w6XgAb3Krk5Vl5q6
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.utils import to_categorical
import tensorflow as tf

# Load dataset
data = pd.read_csv('/emotions.csv.zip')

# Display dataset size
print(f"Dataset size: {len(data)}")

# Separate features and target
X = data.drop(columns=['label'])
y = data['label']

# Encode string labels to integers
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
print("Encoded labels:", np.unique(y_encoded))

# Now convert the integer labels to one-hot encoded format
y_cat = to_categorical(y_encoded)

# Preprocessing
X = data.drop(columns=['label'])  # Assuming 'label' is the target column
y = data['label']

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from tensorflow.keras.layers import Input
# Model definition using an Input layer
model = Sequential([
    Input(shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(y_cat.shape[1], activation='softmax')  # Use y_cat.shape[1] for the number of classes
])

# Extract features as a DataFrame
X = data.drop(columns=['label'])

# Check data types
print(X.dtypes)

# Convert all columns to numeric if possible
X = X.apply(pd.to_numeric, errors='coerce')

# Fill missing values (if any)
X.fillna(0, inplace=True)

# Now scale the features (this will convert X into a NumPy array)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_cat, test_size=0.2, random_state=42)

# Compile the model before training
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Evaluate model
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_test, axis=1)

print(classification_report(y_true_classes, y_pred_classes))
sns.heatmap(confusion_matrix(y_true_classes, y_pred_classes), annot=True, fmt='d')
plt.show()
