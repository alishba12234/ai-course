import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load the dataset
df = pd.read_csv('C:\\Users\\Lenovo\\Documents\\GitHub\\ai-course\\Deep Learning-projects\\AirPassengers[1].csv')
df.head()

# Preprocess the data
df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)
passengers = df['#Passengers'].astype(float).values.reshape(-1, 1)

#Visualize data
plt.figure(figsize=(12,6))
plt.plot(df, label="Passengers")
plt.title("Monthly Airline Passengers")
plt.xlabel("Year")
plt.ylabel("Number of Passengers")
plt.legend()
plt.show()
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(df[["#Passengers"]])

def create_sequences(data, time_steps=12):
    X, y = [], []
    for i in range(len(data)-time_steps):
        X.append(data[i:i+time_steps, 0])
        y.append(data[i+time_steps, 0])
    return np.array(X), np.array(y)

time_steps = 12
X, y = create_sequences(scaled_data, time_steps)
X = X.reshape((X.shape[0], X.shape[1], 1))
train_size = int(len(X) * 0.8)
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Build the LSTM model
model = Sequential([
    LSTM(50, activation='tanh', input_shape=(time_steps,1)),
    Dense(1)
])

model.compile(optimizer='adam', loss='mse')
model.summary()
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=16,
    validation_data=(X_test, y_test),
    verbose=1
)