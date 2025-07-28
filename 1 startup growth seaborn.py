import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("startup_growth data.csv", delimiter=",")
#df.columns = ['Investment Amount ','Funding Rounds', 'Name','Industry','Country']
print(df)

lp = sns.lineplot( data=df , x= "Funding Rounds", y="Investment Amount ")
plt.show()

wait = input ("wait")