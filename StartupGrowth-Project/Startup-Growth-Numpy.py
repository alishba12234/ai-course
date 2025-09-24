# startup_growth.csv
import numpy as np

Industry, FundingRounds , InvestmentAmount ,NumberofInvestors = np.genfromtxt('C:\\Users\\Lenovo\\Documents\\GitHub\\ai-course\\StartupGrowth-project\\startup_growth data.csv', delimiter=',', usecols=(1,2,4,3), unpack=True, dtype=None,skip_header=1,invalid_raise=False)

print(Industry)
print(FundingRounds)
print(InvestmentAmount)
print(NumberofInvestors)

# startup_growth InvestmentAmount - statistics operations

print("startup_growth InvestmentAmount mean: " , np.mean(InvestmentAmount))
print("startup_growth InvestmentAmount average: " , np.average(InvestmentAmount ))
print("startup_growth InvestmentAmount std: " , np.std( InvestmentAmount ))
print("startup_growth InvestmentAmount mod: " , np.median(InvestmentAmount)) 
print("startup_growth InvestmentAmount percentile - 25: " , np.percentile( InvestmentAmount ,25))
print("startup_growth InvestmentAmount percentile  - 75: " , np.percentile( InvestmentAmount ,75))
print("startup_growth InvestmentAmount percentile  - 3: " , np.percentile( InvestmentAmount ,3))
print("startup_growth InvestmentAmount min : " , np.min(InvestmentAmount))
print("startup_growth InvestmentAmount max : " , np.max(InvestmentAmount))


# Calculate and print statistics
print("startup_growth InvestmentAmount mean:", np.mean(InvestmentAmount))
print("InvestmentAmount std dev:", np.std(InvestmentAmount))
print("InvestmentAmount min:", np.min(InvestmentAmount))
print("InvestmentAmount max:", np.max(InvestmentAmount))

# startup_growth InvestmentAmount - maths operations
print("startup_growth InvestmentAmount square: " , np.square(InvestmentAmount))
print("startup_growth InvestnentAmount sqrt: " , np.sqrt(InvestmentAmount))
print("startup_growth InvestmentAmount pow: " , np.power(InvestmentAmount,InvestmentAmount))
print("startup_growth InvestmentAmount abs: " , np.abs(InvestmentAmount))



# Perform basic arithmetic operations
addition = InvestmentAmount+ NumberofInvestors
subtraction = InvestmentAmount - NumberofInvestors
multiplication = InvestmentAmount* NumberofInvestors
division = InvestmentAmount/ NumberofInvestors

print("startup_growth InvestmentAmount - NumberofInvestors - Addition:", addition)
print(" startup_growth InvestmentAmount - NumberofInvestors - Subtraction:", subtraction)
print(" startup_growth InvestmentAmount- NumberofInvestors - Multiplication:", multiplication)
print(" startup_growth InvestmentAmount- NumberofInvestors- Division:", division)


#Trigonometric Function
InvestmentAmountpie =(InvestmentAmount/np.pi)
# Calculate sine, cosine, and tangent
sine_values = np.sin(InvestmentAmountpie)
cosine_values = np.cos(InvestmentAmountpie)
tangent_values = np.tan(InvestmentAmountpie)

print("startup_growth InvestmentAmount - div - pie  - Sine values:", sine_values)
print("startup_growth InvestmentAmount - div - pie Cosine values:", cosine_values)
print("startup_growth InvestmentAmount - div - pie Tangent values:", tangent_values)

print("startup_growth InvestmentAmount - div - pie  - Exponential values:", np.exp(InvestmentAmountpie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(InvestmentAmountpie)
log10_array = np.log10(InvestmentAmountpie)

print(" startup_growth InvestmentAmount - div - pie  - Natural logarithm values:", log_array)
print("startup_growth InvestmentAmount- div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(InvestmentAmountpie)
print("startup_growth  InvestmentAmount - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(InvestmentAmountpie)
print("startup_growth  InvestmentAmount - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(InvestmentAmountpie)
print("startup_growth InvestmentAmount - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(InvestmentAmountpie)
print("startup_growth InvestmentAmount- div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(InvestmentAmountpie)
print("startup_growth InvestmentAmount - div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


# RealEstate bed Plus price - 2 dimentional arrary
D2InvestmentAmountNumberofInvestors = np.array([InvestmentAmountpie,NumberofInvestors])

print ("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - " ,D2InvestmentAmountNumberofInvestors)

# check the dimension of array1
print("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - dimension" , D2InvestmentAmountNumberofInvestors.ndim) 
# Output: 2

# return total number of elements in array1
print("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - total number of elements" ,D2InvestmentAmountNumberofInvestors.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - gives size of array in each dimension" ,D2InvestmentAmountNumberofInvestors.shape)
# Output: (2,3)

# check the data type of array1
print("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - data type" ,D2InvestmentAmountNumberofInvestors.dtype) 
# Output: int64

# Splicing array
D2InvestmentAmountNumberofInvestorsSlice=  D2InvestmentAmountNumberofInvestors[:1,:5]
print("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - Splicing array - D2InvestmentAmountNumberofInvestors[:1,:5] " , D2InvestmentAmountNumberofInvestorsSlice)
D2InvestmentRoundsNumberofInvestorsSlice2=  D2InvestmentAmountNumberofInvestorsSlice[:1, 4:15:4]
print("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - Splicing array - D2InvestmentAmountNumberofInvestors[:1, 4:15:4] " , D2InvestmentAmountNumberofInvestorsSlice)



# Indexing array
D2InvestmentAmountNumberofInvestorsSliceItemOnly=  D2InvestmentAmountNumberofInvestorsSlice[0,1]
print("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - Index array - D2InvestmentAmountNumberofInvestorsSlice[1,5] " , D2InvestmentAmountNumberofInvestorsSliceItemOnly)
D2InvestmentAmountNumberofInvestorsSlice2ItemOnly=  D2InvestmentAmountNumberofInvestorsSlice[0, 2]
print("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - index array - D2InvestmentAmountNumberofInvestorsSlice2[0, 2] " , D2InvestmentAmountNumberofInvestorsSlice2ItemOnly)


#You should use the builtin function nditer, if you don't need to have the indexes values.
for elem in np.nditer(D2InvestmentAmountNumberofInvestors):
    print(elem)

#EDIT: If you need indexes (as a tuple for 2D table), then:
for index, elem in np.ndenumerate(D2InvestmentAmountNumberofInvestors):
    print(index, elem)

# RealEstate bed Plus price - 2 dimentional arrary - bedprice
rows = np.shape(D2InvestmentAmountNumberofInvestors[0])[0]
cols = np.shape(D2InvestmentAmountNumberofInvestors[1])[0]
for i in range(0, (rows + 1)):
    for j in range(0, (cols + 1)):
        print (D2InvestmentAmountNumberofInvestors[0,1])
#

# 2 x 149 ========>>>>> 1  x 298 - reshape
D2bedInvestorsAmountNumberofInvestors1TO200 =np.reshape(D2InvestmentAmountNumberofInvestors, (1, 200))
print("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - np.reshape(D2InvestmentAmountNumberofInvestor, (1, 298)) : " , D2InvestmentAmountNumberofInvestors)
print("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - np.reshape(D2InvestmentAmountNumberofInvestor, (1, 298)) : Size " , D2InvestmentAmountNumberofInvestors.size)
print("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - np.reshape(D2InvestmentAmountNumberofInvestor, (1, 298)) : ndim " , D2InvestmentAmountNumberofInvestors.ndim)
print("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - np.reshape(D2InvestmentAmountNumberofInvestor, (1, 298)) : shape " , D2InvestmentAmountNumberofInvestors.shape)
print("startup_growth InvestmentAmount Plus NumberofInvestors - 2 dimentional arrary - np.reshape(D2InvestmentAmountNumberofInvestor, (1, 298)) : ndim " , D2InvestmentAmountNumberofInvestors.ndim)




print()

