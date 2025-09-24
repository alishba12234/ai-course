# FastFood - Numpy operations
import numpy as np

Address,City,Country,Longitude,latitude = np.genfromtxt('C:\\Users\\Lenovo\\Documents\\GitHub\\ai-course\\FastFood-project\\FastFoodRestaurants.csv', delimiter = ',',usecols=(0,3,4,5,6),dtype= None,skip_header=1, unpack=True, invalid_raise=False)

print(Address)
print(City)
print(Country)
print(Longitude)
print(latitude)

# FastFood - statistics operation
print("FastFood_restaurant Longitude mean:",np.mean(Longitude))
print("FastFood_restaurant Longitude average:",np.average(Longitude))
print("FastFood_restaurant Longitude std :",np.std(Longitude))
print("FastFood_restaurant Longitude mod:",np.median(Longitude))

# FastFood - maths operation
print("FastFood_restaurant  Longitude mean square:",np.square(Longitude))
print("FastFood_restaurant Longitude  mean sqrt:",np.sqrt(Longitude))
print("FastFood_restaurant Longitude mean pow:",np.power(Longitude,Longitude))
print("FastFood_restaurant Longitude mean abs: " ,np.abs(Longitude))

# perform basic arithematic operation
addition = Longitude,latitude
subtraction = Longitude ,latitude
multiplication = Longitude, latitude
division = Longitude ,latitude

print("FastFood_restaurant Longitude - latitude - Addition :", addition)
print("FastFood_restaurant Longitude - latitude - Subtraction :",subtraction)
print("FastFood_restaurant Longitude - latitude - Multiplication :", multiplication)
print("FastFood_restaurant Longitude - latitude - Division :",division )

# Trigonometric Functions

LongitudePie = (Longitude/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(LongitudePie)
cosine_values = np.cos(LongitudePie)
tangent_values = np.tan(LongitudePie)

print("FastFood_restaurant Longitude- div - pie  - Sine values:", sine_values)
print("FastFood_restaurant Longitude - div - pie Cosine values:", cosine_values)
print("FastFood_restaurant Longitude- div - pie Tangent values:", tangent_values)

print("FastFood_restaurant Longitude - div - pie  - Exponential values:", np.exp(LongitudePie))

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(LongitudePie)
log10_array = np.log10(LongitudePie)

print("FastFood_restaurant - div - pie  - Natural logarithm values:", log_array)
print("FastFood_restaurant - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(LongitudePie)
print("FastFood_restaurant Longitude - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(LongitudePie)
print(" FastFood_restaurant - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(LongitudePie)
print("FastFood_restaurant Longitude - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(LongitudePie)
print("FastFood_restaurant - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(LongitudePie)
print("FastFood_restaurant - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#FastFood Longitude Plus Latitude - 2 dimentional arrary
D2LongLat = np.array([Longitude,latitude])

print ("FastFood_restaurant Longitude Plus Latitude - 2 dimentional arrary - " ,D2LongLat)

# check the dimension of array1
print("FastFood_restaurant Longitude Plus Latitude- 2 dimentional arrary - dimension" , D2LongLat.ndim) 
# Output: 2

# return total number of elements in array1
print("FastFood_restaurant Longitude Plus Latitude - 2 dimentional arrary - total number of elements" ,D2LongLat.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("FastFood_restaurant Longitude Plus Latitude - 2 dimentional arrary - gives size of array in each dimension" ,D2LongLat.shape)
# Output: (2,3)

# check the data type of array1
print("FastFood_restaurant Longitude  Plus Latitude - 2 dimentional arrary - data type" ,D2LongLat.dtype) 
# Output: int64

# Splicing array
D2LongLatSlice=  D2LongLat[:1,:6]
print("FastFood_ restaurant Longitude Plus Latitude - 2 dimentional arrary - Splicing array - D2LongLat[:1,:5] " , D2LongLatSlice)




