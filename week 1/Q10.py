# Salary Calculator
# # Input basic salary
basic_salary = float(input("Enter Basic Salary:"))

# Calculate HRA (20%) and DA (15%)
hra = 0.20 * basic_salary
da = 0.15 * basic_salary

# Total Salary
total_salary = basic_salary + hra + da

# Display results
print("\nBasic Salary =", basic_salary)
print("HRA (20%) =", hra)
print("DA (15%) =", da)
print("Total Salary =", total_salary)
