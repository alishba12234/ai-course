# BMI Calculator
# Input values
weight = float(input("Enter weight (in kg): "))
height = float(input("Enter height (in meters): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display result
print(f"\nYour BMI = {bmi:.2f}")
