import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load dataset (fixed path issue)
df = pd.read_csv('C:\\Users\\Lenovo\\Documents\\GitHub\\ai-course\\RealEstate-2001\\Real_Estate_Sales_2001.csv')
# Step 1: Select features and target
X = df[["Assessed Value"]].values
y = df["Sale Amount"].values

# Step 2: Split into 90% train and 10% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Step 3: Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Get intercept and slope
intercept = model.intercept_
slope = model.coef_[0]

print("Intercept:", intercept)
print("Slope:", slope)

# Step 5: Define custom prediction function
def predict_sale_amount(assessed_value, slope, intercept):
    return intercept + slope * assessed_value

# Example: Predict for 3 values
sample_values = X_train[:3].flatten()
manual_preds = [predict_sale_amount(val, slope, intercept) for val in sample_values]
print("Manual Predictions:", manual_preds)

# Step 6: Predict on test set
y_pred = model.predict(X_test)

# Step 7: Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

# Step 8: Plot regression line
plt.figure(figsize=(8,6))
plt.scatter(X, y, color="blue", alpha=0.5, label="Actual Data")
plt.plot(X, model.predict(X), color="red", linewidth=2, label="Regression Line")
plt.xlabel("Assessed Value")
plt.ylabel("Sale Amount")
plt.title("Linear Regression: Assessed Value vs Sale Amount")
plt.legend()
plt.show()