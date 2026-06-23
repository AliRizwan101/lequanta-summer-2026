marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("Marks: ", marks)
print("Grade: ", grade)

if marks >= 60:
    print("You passed.")
else:
    print("You failed.")