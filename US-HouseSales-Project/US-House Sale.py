import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('C:\\Users\\Lenovo\\Documents\\GitHub\\ai-course\\US-HouseSales-project\\us_house_Sales_data.csv')

#  Data Cleaning
# Price
df["Price"] = df["Price"].replace('[\$,]', '', regex=True).astype(float)

# Bedrooms
df["Bedrooms"] = df["Bedrooms"].str.replace(" bds", "").astype(float)

# Bathrooms 
df["Bathrooms"] = df["Bathrooms"].str.replace(" ba", "").astype(float)

# Area 
df["Area (Sqft)"] = df["Area (Sqft)"].str.replace(" sqft", "").str.replace(",", "").astype(float)

# Lot Size 
df["Lot Size"] = df["Lot Size"].str.replace(" sqft", "").str.replace(",", "").astype(float)

# Feature selection

features = ["Bedrooms", "Bathrooms", "Area (Sqft)", "Lot Size", "Year Built", "Days on Market"]
X = df[features]
y = df["Price"]

#  Train/test split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
# Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)


# Evaluation
def evaluate(y_true, y_pred, model_name):
    print(f"\n{model_name} Results:")
    print("R² Score:", r2_score(y_true, y_pred))
    print("MSE:", mean_squared_error(y_true, y_pred))

evaluate(y_test, y_pred_lr, "Linear Regression")


# Visualization
plt.figure(figsize=(10,5))
plt.scatter(y_test, y_pred_lr, alpha=0.6, label="Linear Regression", color="red")
plt.plot([y.min(), y.max()], [y.min(), y.max()], "k--", lw=2)  # perfect line
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.legend()
plt.show()
