#startup_1
import numpy as np

Name,Industry,FundingRounds,InvestmentAmount = np.genfromtxt('startup_growth_investment_data.csv', delimiter=',', usecols=(0,3,4,5),dtype=None,skip_header=1,unpack=True,invalid_raise=False)
print(Name)
print(Industry)
print(FundingRounds)
print(InvestmentAmount)
# startup growth - statistics operations
print("startup_1 InvestmentAmount mean: " , np.mean(InvestmentAmount))
print("startup_1 InvestmentAmount average: " , np.average(InvestmentAmount))
print("startup_1 InvestmentAmount std: " , np.std(InvestmentAmount))
print("startup_1 InvestmentAmount mod: " , np.median(InvestmentAmount))
print("startup_1 InvestmentAmount percentile - 25: " , np.percentile(InvestmentAmount,25))
print("startup_1 InvestmentAmount percentile  - 75: " , np.percentile(InvestmentAmount,75))
print("startup_1 InvestmentAmount percentile  - 3: " , np.percentile(InvestmentAmount,3))
print("startup_1 InvestmentAmount min : " , np.min(InvestmentAmount))
print("startup_1 InvestmentAmount max : " , np.max(InvestmentAmount))

# startup growth - maths operations
print("startup_1 InvestmentAmount mean square: " , np.square(InvestmentAmount))
print(" startup_1 InvestmentAmount mean sqrt: " , np.sqrt(InvestmentAmount))
print("startup_1 InvestmentAmount mean pow: " , np.power(InvestmentAmount,InvestmentAmount))
print("startup_1 InvestmentAmount mean abs: " , np.abs(InvestmentAmount))

# perform basic arithmetic operation
addition = FundingRounds + InvestmentAmount
subtraction = FundingRounds - InvestmentAmount
multiplication = FundingRounds*InvestmentAmount
division = FundingRounds / InvestmentAmount

print(" startup_1 FundingRounds - InvestmentAmount - Addition:", addition)
print(" startup_1 FundingRounds - InvestmentAmount - Subtraction:", subtraction)
print(" startup_1 FundingRounds - InvestmentAmount - Multiplication:", multiplication)
print(" startup_1 FundingRounds - InvestmentAmount - Division:", division)


#Trigonometric Functions

InvestmentAmountPie = (InvestmentAmount/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(InvestmentAmountPie)
cosine_values = np.cos(InvestmentAmountPie)
tangent_values = np.tan(InvestmentAmountPie)

print("startup_1 InvestmentAmount - div - pie  - Sine values:", sine_values)
print("startup_1 InvestmentAmount - div - pie Cosine values:", cosine_values)
print("startup_1 InvestmentAmount - div - pie Tangent values:", tangent_values)

print("startup_1 InvestmentAmount- div - pie  - Exponential values:", np.exp(InvestmentAmountPie))

# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(InvestmentAmountPie)
log10_array = np.log10(InvestmentAmountPie)

print("startup_1 InvestmentAmount - div - pie  - Natural logarithm values:", log_array)
print("startup_1 InvestmentAmount - div - pie  = Base-10 logarithm values:", log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(InvestmentAmountPie)
print("startup_1 InvestmentAmount - div - pie   - Hyperbolic Sine values:", sinh_values)


#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(InvestmentAmountPie)
print(" startup_1 InvestmentAmount - div - pie   - Hyperbolic Cosine values:", cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(InvestmentAmountPie)
print("startup_1 InvestmentAmount - div - pie   -Hyperbolic Tangent values:", tanh_values)

#Example: Inverse Hyperbolic Sine

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(InvestmentAmountPie)
print("startup_1 InvestmentAmount - div - pie   -Inverse Hyperbolic Sine values:", asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(InvestmentAmountPie)
print(" startup_1 InvestmentAmount- div - pie   -Inverse Hyperbolic Cosine values:", acosh_values)


#startup_1 FundingRounds Plus InvestmentAmount - 2 dimentional arrary
D2LongLat = np.array([FundingRounds,InvestmentAmount])

print ("startup_1 FundingRounds Plus InvestmentAmount - 2 dimentional arrary - " ,D2LongLat)

# check the dimension of array1
print("startup_1  FundingRound Plus InvestmentAmount- 2 dimentional arrary - dimension" , D2LongLat.ndim) 
# Output: 2

# return total number of elements in array1
print(" startup_1 FundingRound Plus InvestmentAmount - 2 dimentional arrary - total number of elements" ,D2LongLat.size)
# Output: 6

# return a tuple that gives size of array in each dimension
print("startup_1 FundingRound  Plus InvestmentAmount - 2 dimentional arrary - gives size of array in each dimension" ,D2LongLat.shape)
# Output: (2,3)

# check the data type of array1
print(" startup_1 FundingRound Plus InvestmentAmount - 2 dimentional arrary - data type" ,D2LongLat.dtype) 
# Output: int64

# Splicing array
D2LongLatSlice=  D2LongLat[:1,:5]
print("startup_1 FundingRound  Plus InvestmentAmount - 2 dimentional arrary - Splicing array - D2LongLat[:1,:5] " , D2LongLatSlice)


