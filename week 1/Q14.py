# Percentage of Correct Answers
# Input values
total_questions = int(input("Enter total number of questions: "))
correct_answers = int(input("Enter number of correct answers: "))

# Calculate percentage
percentage = (correct_answers / total_questions) * 100

# Display result
print(f"\nPercentage Score = {percentage:.2f}%")
