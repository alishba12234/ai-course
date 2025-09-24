from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import pandas as pd

# Load fie
df = pd.read_csv('C:\\Users\\Lenovo\\Documents\\GitHub\\ai-course\\Zameen.com-project\\zameencom_property_data.csv', sep=";")

# Select feature (X) and target (y)
X = ["bedrooms"]
y = ["price"]

# Split data into train (75%) and test (25%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Get intercept and slope
intercept = model.intercept_
slope = model.coef_[0]

# Predictions
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

(intercept, slope, mae, mse, rmse, y_test.head().to_dict(), y_pred[:5])