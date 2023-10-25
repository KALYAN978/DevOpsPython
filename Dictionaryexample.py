student_scores = {
    "Harry": 81,
    "Ron": 87,
    "Draco": 81,
    "Herive": 62,
    }

#Creating an empty dictionary
student_grades = {}

#Converting scores in to grades
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score >80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)