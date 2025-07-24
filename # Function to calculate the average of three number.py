# Function to calculate the average of three numbers

def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3)

# Take user input for three numbers
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
num3 = float(input("Enter the third number: "))

# Calculate the average
average = ((num1+num2+num3)/2)

# Print the result
print("The average of the three numbers is:",average)