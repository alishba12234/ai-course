import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\Lenovo\\Documents\\GitHub\\ai-course\\FastFood-project\\FastFoodRestaurants.csv',delimiter= ",")
#df.columns = ['address','city', 'country','longitude','latitude']
print(df)

lp = sns.lineplot( data=df , x= "longitude", y="latitude")
plt.show()

wait = input ("wait")