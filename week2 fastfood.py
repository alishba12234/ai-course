#fastfood_restaurant
import numpy as np

addressV2,cityV2,lV2,uV2 = np.genfromtxt('FastFoodRestaurants.csv', delimiter = ',',usecols=(0,3,4,5),dtype=None,skip_header=1, unpack=True, invalid_raise=False)

print(addressV2)
print(cityV2)
print(lV2)
print(uV2)