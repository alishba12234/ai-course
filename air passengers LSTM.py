import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from keras.metrics import Precision, Recall

data = pd.read_csv('AirPassengers[1].csv')
data['Month'] = pd.to_datetime(data['Month'])
data.set_index('Month', inplace=True)
passengers = data['#Passengers'].astype(float).values.reshape(-1, 1)

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(passengers)

window_size = 12
X = []
y = []
target_dates = data.index[window_size:]

for i in range(window_size, len(scaled_data)):
    X.append(scaled_data[i - window_size:i, 0])
    y.append(scaled_data[i, 0])

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test, dates_train, dates_test = train_test_split(
    X, y, target_dates, test_size=0.2, shuffle=False
)

X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

model = Sequential()
model.add(LSTM(units=128 , return_sequences=True , input_shape=(X_train.shape[1] , 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=128))
model.add(Dropout(0.2))
model.add(Dense(1))

METRICS = metrics = ['accuracy' ,
                    Precision(name='precision') ,
                    Recall(name='recall')]

model.compile(optimizer='adam' , loss='mean_squared_error' , 
              metrics = METRICS)

history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.1)

predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions).flatten()
y_test = scaler.inverse_transform(y_test.reshape(-1,1)).flatten()

rmse = np.sqrt(np.mean((y_test - predictions)**2))
print(f'RMSE: {rmse:.2f}')

plt.figure(figsize=(12, 6))
plt.plot(dates_test, y_test, label='Actual')
plt.plot(dates_test, predictions, label='Predicted')
plt.title('Actual vs Predicted Air Passengers')
plt.xlabel('Month')
plt.ylabel('Passengers')
plt.legend()
plt.show()
read = input("wait")