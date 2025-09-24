# Convert Minutes to Hours and Minutes
# Input minutes
minutes = int(input("Enter total minutes: "))

# Conversion
hours = minutes // 60
remaining_minutes = minutes % 60

# Display result
print(f"\n{minutes} minutes = {hours} hours {remaining_minutes} minutes")
