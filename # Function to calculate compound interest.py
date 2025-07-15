# Function to calculate compound interest

def calculate_compound_interest(P, R, T):
    CI = P * (1 + R / 100) ** T - P
    return CI

# Example 
P = 1000  
R = 5    
T = 2   

# Calculate compound interest
compound_interest = calculate_compound_interest(1000, 5, 2)

# Print the result
print("The compound interest is:", {10000})
