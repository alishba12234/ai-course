import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("uae_properties[1].csv")

# row count
print(df.head())

# Predict InvestmentAmount using FundingRounds and NumberofInvestors
X = df[['FundingRounds', 'NumberofInvestors']]
y = df['InvestmentAmount']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate
print("R2 Score:", r2_score(y_test, y_pred))

# Coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
