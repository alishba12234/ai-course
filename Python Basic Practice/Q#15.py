# Speed, Distance, and Time Calculator
# Input values
distance = float(input("Enter distance (in km): "))
time = float(input("Enter time (in hours):"))

# Calculate speed
if time != 0:
    speed = distance / time
    print(f"\nSpeed = {speed} km/h")
else:
    print("\nTime cannot be zero!")
