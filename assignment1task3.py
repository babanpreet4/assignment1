# Task 3: Grade Calculator

# Accept marks for three subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

# Calculate total and percentage
total = sub1 + sub2 + sub3
percentage = (total / 300) * 100   # Assuming each subject is out of 100

# Determine grade
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "F"

# Print results
print("\n----- Result -----")
print(f"Total Marks: {total}/300")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
