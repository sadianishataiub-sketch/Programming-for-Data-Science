#  LAB-2 EXERCISE 1

data_processing = float(input("Enter your data processing grade: "))
pds = float(input("Enter your data pds: "))
data_science = float(input("Enter your data science grade: "))
python = float(input("Enter your python grade: "))

course_marks = [data_processing, pds, data_science, python]


total = 0
maximum = course_marks[0]
minimum = course_marks[0]
for mark in course_marks:
    total =+ mark
    total_marks  = total

    if mark > maximum :
        highest_grade = mark
        

    if mark < minimum:
        lowest_grade = mark

average_grade = total_marks / len(course_marks)


print(f"highest mark {highest_grade}")
print(f"lowest mark {lowest_grade}")
print(f"average mark {average_grade}")
