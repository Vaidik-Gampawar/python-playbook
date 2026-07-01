'''
Populate a dictionary with six student names and their corresponding
marks. Loop through it and print the names of all students who achieved
a score above 75.
'''

students = {
    "vaidik": 89,
    "lobhas": 78,
    "faiz": 56,
    "sumit": 76,
    "rohan": 52,
    "karan": 79,
    "sakib": 90
}

for name in students:
    if students[name] > 75:
        print(f"{name}: {students[name]}")