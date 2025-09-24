import pandas as pd

# Load and clean the dataset
df = pd.read_csv('C:\\Users\\Lenovo\\Documents\\GitHub\\ai-course\\StartupGrowth-project\\startup_growth data.csv',quotechar='"', on_bad_lines='skip' )


# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Display basic info
print(df)
print("Data Types:\n", df.dtypes)
print("\nDataFrame Info:")
df.info()
print()

# Display first and last 3 rows
print("First three rows:")
print(df.head(3))
print()

print("Last three rows:")
print(df.tail(3))
print()

# Summary statistics and shape
print("Summary of statistics of dataframe:\n", df.describe())
print("Total rows and columns in dataframe:", df.shape)
print()

# Accessing one column
price = df['Funding Rounds']
print("Accessing 'Funding Rounds' column:")
print(price.head())
print()

# Accessing multiple columns
selected_cols = df[['Investment Amount', 'Year Founded', 'Growth Rate (%)']]
print("Accessing multiple columns:")
print(selected_cols.head())
print()

# .loc operations
print("Single row at index 2:")
print(df.loc[2])
print()

print("Multiple rows at indices 1 and 3:")
print(df.loc[[1, 3]])
print()

# Note: Replace 'state', 'bed', 'bath' with actual column names in your CSV if needed
if 'state' in df.columns:
    print("Rows where state == 'Adjuntas':")
    print(df.loc[df['state'] == "Adjuntas"])
    print()

# .iloc examples
print("Row at index 1 using iloc:")
print(df.iloc[1])
print()

print("Multiple rows (2, 3, 5) using iloc:")
print(df.iloc[[2, 3, 5]])
print()

print("Slice of rows 1 to 3 using iloc:")
print(df.iloc[1:4])
print()

print("Column at index 3 using iloc:")
print(df.iloc[:, 3])
print()

# Fill missing values
df.fillna(0, inplace=True)
print("Data after filling NaN with 0:\n", df.head())