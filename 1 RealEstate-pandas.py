import pandas as pd
df = pd.read_csv("C:\\Users\\Lenovo\\Documents\\GitHub\\ai-course\\RealEstate-USA.csv")

print(df)
print("df - Data Type :" , df.dtypes)
print("df.info() : " , df.info())
print()

print("Last three rows:")
print(df.tail(3))
print()

print("First three rows:")
print(df.head(3))
print()

print("Summary of statistics of dataframe:" , df.describe())
print("Total rows and columns in dataframe :" , df.shape)
print()

# for one coloumn
price=df['price']
print("Access the name coloumn :")
print('street')
print()

# access multiple coloumns
price_bed = df[['price' , 'bed']]
print("Access multiple coloumns :")
print(price_bed)
print()

# .loc operations
single_row = df.loc[2]
print("single row :" , single_row)

multiple_rows = df.loc[[1,3]]
print("multiple rows :" , multiple_rows)

rows_2 = df.loc[df['state'] == "Adjuntas"]
print("Conditional selection of rows :", rows_2)

rows_3 = df.loc[1, 'state']
print("selecting single coloumn :" , rows_3)

rows_4 = df.loc[2 : 4, ['bed' , 'bath']]
print("selecting multiple coloumns :" , rows_4)

rows_5 = df.loc[1 : 3 , 'bed' : 'bath']
print("selecting slice of coloumns :" , rows_5)

rows_6 = df.loc[df['state'] == "Adjuntas" , 'bed' : 'zip_code']
print("combined row and coloumn selection :" , rows_6)
print()

# CASE 2 : using .loc with index_col

df_index_col = pd.read_csv("C:\\Users\\Lenovo\\Documents\\GitHub\\ai-course\\RealEstate-USA.csv", delimiter=",")


print(df_index_col)
print(df_index_col.dtypes)
print(df_index_col.info())

row_1 = df_index_col.loc[5]
print("selecting a single row :" , row_1)

# CASE 3 : using .iloc

row_1 = df_index_col.iloc[1]
print("Single row using iloc : ", row_1)

row_2 = df_index_col.iloc[[2, 3, 5]]
print("Selecting multiple rows : ", row_2)

row_3 = df_index_col.iloc[1 : 3]
print("Selecting a slice of rows : ", row_3)

row_4 = df_index_col.iloc[:, 3]
print("Selecting single column : ", row_4)

row_5 = df_index_col.iloc[:, [2, 4]]
print("Selecting multiple columns : ", row_5)

row_6 = df_index_col.iloc[:, 3 : 5]
print("Selecting a slice of columns : ", row_6)

row_7 = df_index_col.iloc[[2, 3, 4], 1 : 5]
print("Combined rows and columns : ", row_7)

# Next Run

# add a new row
#103378,for_sale,105000,3,2,0.12,1962661,Adjuntas,Puerto Rico,601,920,

df.loc[len(df.index)] = [103378, "for_sale", 105000, 3, 2, 0.12,1962661, "Adjuntas", "Puerto Rico", 601, 920, None]

print("Modified DataFrame :")
print(df)
print()

# Remove rows/columns from pandas DataFrame

# delete row with index 2
df.drop(2 , axis=0 , inplace=True)
# delete row with index 3
df.drop(index=3 , inplace=True)
# delete row with index 3 & 5
df.drop([1 , 5] , axis=0 , inplace=True)
print("Modified Dataframe Delete Rows : " , df)

# delete city column
df.drop('status' , axis=1 , inplace=True)
# delete keys column
df.drop(columns='city' , inplace=True)
print("Modified Data Frame :")
print(df)

# Rename labels in a DataFrame
df.rename(columns={'status' : 'status_name'} , inplace=True)
# Rename multiple columns
df.rename(mapper={'brokered_by' : 'separated_by' , 'status' : 'status_name'} , axis=1 , inplace=True)
print("Modified DataFrame :")
print(df)

# Rename rows in a DataFrame
df.rename(index={1 : 5} , inplace=True)
# Rename multiple rows in DataFrame
df.rename(mapper={2 : 6 , 3 : 7} , axis=0 , inplace=True)
print("Modified DataFrame :")
print(df)

# query() to select data
selected_rows = df.loc[(df['bed'] == 3) & (df['bath'] == 2)]
print(selected_rows.to_string())
print(len(selected_rows))

# sort DataFrame by price in ascending order
sorted_df = df.sort_values(by='street')
print(sorted_df.to_string(index=False))

df1 = df.sort_values(by=['street', 'bed'])
print(df1.to_string(index=False))

# group by operations
grouped = df.groupby('bed')['price'].sum()
print(grouped.to_string())
print("grouped : ", len(grouped))

# PANDAS DATA CLEANING
df_cleaned = df.dropna()
print("Cleaned Data \n" , df_cleaned)

df.fillna(0 , inplace=True)
print("Data after filling NaN with 0 : \n" , df)

# create a list named data
data = [3 , 4 , 5 , 6]
array1 = pd.array(data)
print(array1)

int_array = pd.array([1 , 2 , 3 , 3 , 4 , 5], dtype='int')
print(int_array)
print()
