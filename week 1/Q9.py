# Total Marks, Percentage and Average

# Input marks of 5 subjects
marks1 = float(input("Enter marks of Subject 1:"))
marks2 = float(input("Enter marks of Subject 2:"))
marks3 = float(input("Enter marks of Subject 3:"))
marks4 = float(input("Enter marks of Subject 4:"))
marks5 = float(input("Enter marks of Subject 5:"))

# Total marks
total = marks1 + marks2 + marks3 + marks4 + marks5

# Assuming each subject is out of 100
percentage = (total / 500) * 100
average = total / 5

# Display results
print("\nTotal Marks =", total)
print("Percentage =", percentage, "%")
print("Average Marks =", average)
