# Distribute Items Equallay
# Input values
n = int(input("Enter total number of candies: "))
k = int(input("Enter number of students: "))

# Calculate distribution
each_gets = n // k     # Candies each student gets
left = n % k           # Candies left undistributed

# Display results
print("Each student gets:", each_gets, "candies")
print("Candies left:", left)
