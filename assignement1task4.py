# Mini Project: Student Report Card Generator

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

# Input student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

marks = []
for i in range(1, 6):
    while True:
        try:
            mark = float(input(f"Enter marks for Subject {i} (0-100): "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("❌ Invalid input! Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Please enter a valid number.")

# Calculations
total = sum(marks)
average = total / 5
grade = calculate_grade(average)

# Display formatted report card
print("\n-------------------------")
print("     Student Report Card ")
print("-------------------------")
print(f"Name   : {name}")
print(f"Roll No: {roll_no}")
print(f"Total  : {total}")
print(f"Average: {average:.2f}")
print(f"Grade  : {grade}")
print("-------------------------")
