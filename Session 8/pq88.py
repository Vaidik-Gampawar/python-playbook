'''
Design a dictionary where each key is a student's name and the
corresponding value is a list of their marks in 3 different subjects. Calculate
and print the total marks and average marks for each student.
'''

students = {
    "vaidik": [87, 34, 22],
    "lobhas": [55, 65, 89],
    "sumit": [67, 98, 54]
}

for name, marks in students.items():
    total = sum(marks)
    avg = total / len(marks)

    print(f"{name} has scored {total} and average {avg:.2f}")