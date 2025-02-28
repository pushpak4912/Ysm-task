# Program to determine the grade based on the score

score = float(input("Enter your score (0-100): "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"
else:
    grade = "Invalid score. Please enter a number between 0 and 100."


print(f"Your grade is: {grade}")
