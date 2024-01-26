number_of_students = int(input())

students_names_and_grades = {}

# Collecting student names and their grades
for _ in range(number_of_students):
    current_student_name, current_student_grade = input().split()
    current_student_grade = float(current_student_grade)

    if current_student_name not in students_names_and_grades:
        students_names_and_grades[current_student_name] = []
    students_names_and_grades[current_student_name].append(current_student_grade)

# Displaying each student, their grades, and the average grade
for student, grades in students_names_and_grades.items():
    average_grade = sum(grades) / len(grades)
    # Format each grade in the list to two decimal places and join with a space
    student_grades = " ".join(f"{grade:.2f}" for grade in grades)
    print(f"{student} -> {student_grades} (avg: {average_grade:.2f})")
