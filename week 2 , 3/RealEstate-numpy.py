#RealEstate_USA.csv
import numpy as np

bed, price , zip_code , status = np.genfromtxt('RealEstate-USA.csv', delimiter=',', usecols=(3,2,9,1), unpack=True, dtype=None,skip_header=1)

print(bed)
print(price)
print(zip_code)
print(status)

# RealEstate price  - statistics operations
print("RealEstate Price mean: " , np.mean(price))
print("RealEstate Price average: " , np.average(price))
print("RealEstate Price std: " , np.std(price))
print("RealEstate Price mod: " , np.median(price))
print("RealEstate Price percentile - 25: " , np.percentile(price,25))
print("RealEstate Price percentile  - 75: " , np.percentile(price,75))
print("RealEstate Price percentile  - 3: " , np.percentile(price,3))
print("RealEstate Price min : " , np.min(price))
print("RealEstate Price max : " , np.max(price))

# RealEstate price  - maths operations
print("RealEstate Price square: " , np.square(price))
print("RealEstate Price sqrt: " , np.sqrt(price))
print("RealEstate Price pow: " , np.power(price,price))
print("RealEstate Price abs: " , np.abs(price))



# Perform basic arithmetic operations
addition = bed + price
subtraction = bed - price
multiplication = bed* price
division = bed / price

print(" RealEstate bed - price - Addition:", addition)
print(" RealEstate bed - price - Subtraction:", subtraction)
print(" RealEstate bed - price - Multiplication:", multiplication)
print(" RealEstate bed - price - Division:", division)


#Trigonometric Functions

pricePie = (price/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("RealEstate Price - div - pie  - Sine values:", sine_values)
print("RealEstate Price - div - pie Cosine values:", cosine_values)
print("RealEstate Price - div - pie Tangent values:", tangent_values)

print("RealEstate Price - div - pie  - Exponential values:", np.exp(pricePie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print(" RealEstate Price - div - pie  - Natural logarithm values:", log_array)
print("RealEstate Price - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(pricePie)
print(" RealEstate Price - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(pricePie)
print(" RealEstate Price - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(pricePie)
print("RealEstate Price - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(pricePie)
print("RealEstate Price - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(pricePie)
print("RealEstate Price - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


# RealEstate bed Plus price - 2 dimentional arrary
D2bedprice = np.array([bed, price])

print ("RealEstate bed Plus price - 2 dimentional arrary - " ,D2bedprice)

# check the dimension of array1
print("RealEstate bed Plus price - 2 dimentional arrary - dimension" , D2bedprice.ndim) 
# Output: 2

# return total number of elements in array1
print("RealEstate bed Plus price - 2 dimentional arrary - total number of elements" ,D2bedprice.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("RealEstate bed Plus price - 2 dimentional arrary - gives size of array in each dimension" ,D2bedprice.shape)
# Output: (2,3)

# check the data type of array1
print("RealEstate bed plus price - 2 dimentional arrary - data type" ,D2bedprice.dtype) 
# Output: int64

# Splicing array
D2bedpriceSlice=  D2bedprice[:1,:5]
print("RealEstate bed Plus price - 2 dimentional arrary - Splicing array - D2bedprice[:1,:5] " , D2bedpriceSlice)
D2bedpriceSlice2=  D2bedprice[:1, 4:15:4]
print(" RealEstate bed Plus price - 2 dimentional arrary - Splicing array - D2bedprice[:1, 4:15:4] " , D2bedpriceSlice2)



# Indexing array
D2bedpriceSliceItemOnly=  D2bedpriceSlice[0,1]
print("RealEstate bed Plus price - 2 dimentional arrary - Index array - D2bedpriceSlice[1,5] " , D2bedpriceSliceItemOnly)
D2bedpriceSlice2ItemOnly=  D2bedpriceSlice2[0, 2]
print("RealEstate bed Plus price - 2 dimentional arrary - index array - D2bedpriceSlice2[0, 2] " , D2bedpriceSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2bedprice):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2bedprice):
    print(index, elem)

# RealEstate bed Plus price - 2 dimentional arrary - bedprice
rows = np.shape(D2bedprice[0])[0]
cols = np.shape(D2bedprice[1])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print (D2bedprice[0,1])
#

# 2 x 149 ========>>>>> 1  x 298 - reshape
D2bedprice1TO400 =np.reshape(D2bedprice, (1, 400))
print("RealEstate bed Plus price - 2 dimentional arrary - np.reshape(D2bedprice, (1, 298)) : " , D2bedprice1TO400)
print("RealEstate bed Plus price - 2 dimentional arrary - np.reshape(D2bedprice, (1, 298)) : Size " , D2bedprice1TO400.size)
print("RealEstate bed Plus price - 2 dimentional arrary - np.reshape(D2bedprice, (1, 298)) : ndim " , D2bedprice1TO400.ndim)
print("RealEstate bed Plus price - 2 dimentional arrary - np.reshape(D2bedprice, (1, 298)) : shape " , D2bedprice1TO400.shape)
print("RealEstate bed Plus price- 2 dimentional arrary - np.reshape(D2bedprice, (1, 298)) : ndim " , D2bedprice1TO400.ndim)




print()

