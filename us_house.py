# multiple_linear_regression.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

df = pd.read_csv("us_house_Sale_data[1].csv")

# Clean columns
df["Price"] = df["Price"].str.replace("[$,]", "", regex=True).astype(float)
df["Bedrooms"] = df["Bedrooms"].str.replace(" bds", "", regex=True).astype(int)
df["Bathrooms"] = df["Bathrooms"].str.replace(" ba", "", regex=True).astype(int)
df["Area (Sqft)"] = df["Area (Sqft)"].str.replace(" sqft", "", regex=True).astype(int)
df["Lot Size"] = df["Lot Size"].str.replace(" sqft", "", regex=True).astype(int)

# Select features - independent variables
X = df[["Bedrooms", "Bathrooms", "Area (Sqft)", "Lot Size", "Year Built", "Days on Market"]]

# Target variable - dependent variable
y = df["Price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model Evaluation
print("R2 Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# Coefficients
print("\nFeature Coefficients:")
for col, coef in zip(X.columns, model.coef_):
    print(f"{col}: {coef:.2f}")
