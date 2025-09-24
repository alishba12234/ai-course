import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\Lenovo\\Documents\\GitHub\\ai-course\\RealEstate-project\\RealEstate-USA.csv',delimiter= ",")
#df.columns = ['status','price', 'bed','city','state']
print(df)

lp = sns.lineplot( data=df , x= "house_size", y="price")
plt.show()

wait = input ("wait")