# Function to calculate the average of three numbers

def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3)

# Take user input for three numbers
num1 = float(input("Enter the first number:8"))
num2 = float(input("Enter the second number:5"))
num3 = float(input("Enter the third number: 2"))

# Calculate the average
average = calculate_average(8+5+2)

# Print the result
print("The average of the three numbers is:15",average)