'''
Create a dictionary for a student, including keys like name, age,
city, and marks (as a list of scores). Print each piece of
information using its key.
'''

student = {
    "name": "vaidik",
    "age": 21,
    "city": "pune",
    "marks": [45, 76, 78, 45, 45]
}

for k in student.keys():
    print(f"{k}: {student[k]}")